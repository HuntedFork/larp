#!/usr/bin/env python3
"""Check that every mystery clue still fits its fixed-height printed page.

Why this exists
---------------
`.page-inside` in clue-print.css is a fixed 11in box with `overflow: hidden`,
so any text that grows past the bottom is *silently clipped* on the printed
prop — it looks fine in the browser and comes out of the printer missing its
last paragraph. Changing the clue font changes how much room the text needs,
so this script re-measures every clue.

How it measures
---------------
It reads the real advance widths out of the self-hosted woff2 files, greedily
wraps each block at the column width, and sums line boxes plus margins. It is
an estimate — a browser applies kerning, hyphenation and slightly different
rounding — so it reports the used fraction of the page and flags anything
over a safety threshold rather than pretending to be exact.

Usage:  python3 tools/check-clue-fit.py
"""

import glob
import os
import re
import sys
from html.parser import HTMLParser

try:
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
except ImportError:
    sys.exit("fontTools is required: pip install fonttools brotli")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(ROOT, "docs", "shared", "fonts")

# ---------------------------------------------------------------------------
# Font metrics
# ---------------------------------------------------------------------------
_cache = {}


def advances(filename, weight=None):
    """Map of character -> advance width in em units.

    Bold text genuinely measures wider than regular, and the clues carry
    every puzzle fact in <strong>, so the bold widths have to be real:

    - A variable font (EB Garamond) is instanced on its wght axis.
    - A static family (Kalam) ships one file per weight, so BOLD_FILES
      maps to the separate bold file. Without this the bold text would be
      measured at regular width and the estimate would run optimistic.
    """
    if weight is not None and filename in BOLD_FILES:
        filename, weight = BOLD_FILES[filename], None
    key = (filename, weight)
    if key in _cache:
        return _cache[key]
    font = TTFont(os.path.join(FONT_DIR, filename))
    if weight is not None and "fvar" in font:
        font = instancer.instantiateVariableFont(
            font, {"wght": weight}, inplace=False
        )
    upm = font["head"].unitsPerEm
    hmtx = font["hmtx"]
    table = {}
    for code, glyph in font.getBestCmap().items():
        if glyph in hmtx.metrics:
            table[chr(code)] = hmtx[glyph][0] / upm
    _cache[key] = table
    return table


BOOK = "kalam-latin.woff2"
BOOK_ITALIC = "kalam-latin.woff2"  # Kalam has no italic; browsers synthesise a slant
INSCRIPTION = "cinzel-latin.woff2"
HAND = "architectsdaughter-latin.woff2"

# Static families ship one file per weight rather than a wght axis, so a
# bold run has to be measured from its own file.
BOLD_FILES = {
    "kalam-latin.woff2": "kalam-bold-latin.woff2",
}

# ---------------------------------------------------------------------------
# Page geometry (must mirror clue-print.css)
# ---------------------------------------------------------------------------
PAGE_H = 11.0            # .page-inside height
PAD_V = 0.85 * 2         # .page-inside vertical padding
PAD_H = 0.9 * 2          # .page-inside horizontal padding
COLUMN_IN = 8.5 - PAD_H  # usable text column
BUDGET_IN = PAGE_H - PAD_V

PT = 1 / 72.0            # points to inches
BOLD_WEIGHT = 700        # what <strong> resolves to in the clue stylesheet


# Per-block style: font file, size (pt), line-height, space below (in),
# left indent (in). Mirrors the .inside rules in clue-print.css.
BLOCKS = {
    "p":            (BOOK,        10.5, 1.42, 0.07, 0.0),
    "frontispiece": (BOOK,         9.5, 1.42, 0.08, 0.0),
    "margin":       (HAND,         9.5, 1.40, 0.06, 0.27),
    "verse":        (BOOK,        10.5, 1.50, 0.06, 0.2),
    "signoff":      (BOOK,        10.5, 1.42, 0.07, 0.0),
    "h2":           (INSCRIPTION, 10.8, 1.25, 0.05, 0.0),
    "hr":           (None,         0.0, 0.0,  0.16, 0.0),
}


def text_width_em(text, table):
    fallback = table.get("n", 0.5)
    return sum(table.get(ch, fallback) for ch in text)


def wrapped_lines(runs, size_pt, column_in):
    """Greedy line-break count for a list of (text, table) runs.

    Runs let a paragraph mix weights — the clues carry their puzzle facts in
    <strong>, which is measurably wider than the surrounding text.
    """
    limit_em = column_in / (size_pt * PT)
    words = []
    for text, table in runs:
        for word in text.split():
            words.append((text_width_em(word, table), table.get(" ", 0.25)))
    if not words:
        return 0
    lines, current = 1, 0.0
    for width, space in words:
        candidate = width if current == 0 else current + space + width
        if candidate > limit_em and current > 0:
            lines += 1
            current = width
        else:
            current = candidate
    return lines


# ---------------------------------------------------------------------------
# Pull the inside-page blocks out of a clue file
# ---------------------------------------------------------------------------
class InsideParser(HTMLParser):
    """Collect (block-kind, [(text, bold)]) pairs from a clue's `.inside` div."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.in_inside = False
        self.kind = None
        self.bold = 0
        self.buf = []
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "").split()
        if tag == "div":
            if "inside" in classes:
                self.in_inside = True
                self.depth = 1
                return
            if self.in_inside:
                self.depth += 1
            return
        if not self.in_inside:
            return
        if tag == "hr":
            self.blocks.append(("hr", []))
        elif tag in ("p", "h2"):
            self.kind = next((c for c in classes if c in BLOCKS), tag)
            self.buf = []
            self.bold = 0
        elif tag in ("strong", "b") and self.kind:
            self.bold += 1
        elif tag == "br" and self.kind:
            # A hard break starts a new line box; mark it for the wrapper.
            self.buf.append(("\n", False))

    def handle_endtag(self, tag):
        if tag == "div" and self.in_inside:
            self.depth -= 1
            if self.depth == 0:
                self.in_inside = False
            return
        if tag in ("strong", "b") and self.bold:
            self.bold -= 1
        elif self.kind and tag in ("p", "h2"):
            self.blocks.append((self.kind, self.buf))
            self.kind = None
            self.buf = []

    def handle_data(self, data):
        if self.kind:
            self.buf.append((data, self.bold > 0))


def measure(path):
    """Return (inches of vertical space used, number of blocks)."""
    with open(path, encoding="utf-8") as handle:
        parser = InsideParser()
        parser.feed(handle.read())

    total = 0.0
    for kind, parts in parser.blocks:
        font, size, line_h, margin, indent = BLOCKS[kind]
        total += margin
        if font is None:
            continue
        regular = advances(font)
        bold = advances(font, BOLD_WEIGHT)
        column = COLUMN_IN - indent

        # Split the block at hard <br> breaks; each segment wraps on its own.
        segments, current = [], []
        for text, is_bold in parts:
            pieces = text.split("\n")
            for index, piece in enumerate(pieces):
                if index > 0:
                    segments.append(current)
                    current = []
                cleaned = re.sub(r"\s+", " ", piece)
                if cleaned.strip():
                    current.append((cleaned, bold if is_bold else regular))
        segments.append(current)

        lines = sum(wrapped_lines(seg, size, column) for seg in segments)
        total += lines * size * PT * line_h
    return total, len(parser.blocks)


def main():
    files = sorted(
        glob.glob(os.path.join(ROOT, "docs", "mystery", "clue*.html")),
        key=lambda p: int(re.search(r"clue(\d+)", p).group(1)),
    )
    worst = 0.0
    problems = []
    print("Text column %.2fin wide, %.2fin of vertical room per inside page.\n"
          % (COLUMN_IN, BUDGET_IN))
    for path in files:
        used, blocks = measure(path)
        pct = used / BUDGET_IN * 100
        worst = max(worst, pct)
        flag = "OK"
        if pct > 100:
            flag = "OVER"
            problems.append(os.path.basename(path))
        elif pct > 90:
            flag = "TIGHT"
            problems.append(os.path.basename(path))
        print("%-5s %-14s %5.2fin  %5.1f%% of page  (%d blocks)"
              % (flag, os.path.basename(path), used, pct, blocks))

    print("\nFullest page: %.1f%%" % worst)
    if problems:
        print("Needs attention: " + ", ".join(problems))
        return 1
    print("All clues fit with room to spare.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

