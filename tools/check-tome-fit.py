#!/usr/bin/env python3
"""Check that both Cursed Tome inside pages still fit their printed page.

Same problem as the clues: `.page-inside` in cursed-tome-print.css is a fixed
11in box with `overflow: hidden`, so text that grows past the bottom is
*silently clipped* on the printed leaf — it looks fine in the browser and comes
out of the printer missing its last paragraph.

This reuses the measuring machinery in check-clue-fit.py (real advance widths
out of the self-hosted woff2 files) with the Cursed Tome's own block styles.

Usage:  python3 tools/check-tome-fit.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import importlib

fit = importlib.import_module("check-clue-fit")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "docs", "docs", "cursed-tome.html")

PRINTED = "ebgaramond-latin.woff2"

# Page geometry — mirrors .page-inside in cursed-tome-print.css
fit.PAD_V = 0.85 * 2
fit.PAD_H = 0.9 * 2
fit.COLUMN_IN = 8.5 - fit.PAD_H
fit.BUDGET_IN = fit.PAGE_H - fit.PAD_V

# Per-block style: font file, size (pt), line-height, space below (in),
# left indent (in). Mirrors the .inside rules in cursed-tome-print.css.
fit.BLOCKS = {
    "p":           (fit.BOOK,        11.0, 1.45, 0.12, 0.0),
    "reading":     (PRINTED,         11.5, 1.40, 0.22, 0.20),
    "script":      (fit.BOOK,        12.5, 1.55, 0.12, 0.0),
    "dated":       (fit.BOOK,        11.5, 1.45, 0.36, 0.0),
    "signature":   (fit.INSCRIPTION, 12.0, 1.45, 0.22, 0.0),
    "question":    (fit.INSCRIPTION, 20.0, 1.45, 0.65, 0.0),
    "instruction": (PRINTED,         11.0, 1.45, 0.00, 0.0),
    "h2":          (fit.INSCRIPTION, 16.0, 1.45, 0.28, 0.0),
    "hr":          (None,             0.0, 0.00, 0.44, 0.0),
    # .write-lines is 4 ruled lines of 0.42in plus 0.2in below; it carries no
    # text, so it is charged as pure vertical space.
    "write-lines": (None,             0.0, 0.00, 1.88, 0.0),
}


class TomeParser(fit.InsideParser):
    """Also count the ruled writing space, which is a div rather than a p."""

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "").split()
        if tag == "div" and "write-lines" in classes and self.in_inside:
            self.blocks.append(("write-lines", []))
        super().handle_starttag(tag, attrs)


def measure_pages(path):
    """Measure every `.inside` block on the page, split per leaf."""
    with open(path, encoding="utf-8") as handle:
        parser = TomeParser()
        parser.feed(handle.read())

    # Blocks arrive in document order; the two inside pages are separated by
    # the leaf-2 heading. Split on the first "question" block, which only the
    # purified leaf carries.
    blocks = parser.blocks
    split = next(
        (i for i, (kind, _) in enumerate(blocks) if kind == "question"), len(blocks)
    )
    # The purified leaf starts at its own opening .reading block.
    start = max(
        (i for i, (kind, _) in enumerate(blocks[:split]) if kind == "reading"),
        default=split,
    )
    return [blocks[:start], blocks[start:]]


def height(blocks):
    total = 0.0
    for kind, parts in blocks:
        font, size, line_h, margin, indent = fit.BLOCKS[kind]
        total += margin
        if font is None:
            continue
        regular = fit.advances(font)
        bold = fit.advances(font, fit.BOLD_WEIGHT)
        runs = []
        for text, is_bold in parts:
            cleaned = " ".join(text.split())
            if cleaned.strip():
                runs.append((cleaned, bold if is_bold else regular))
        total += fit.wrapped_lines(runs, size, fit.COLUMN_IN - indent) \
            * size * fit.PT * line_h
    return total


def main():
    pages = measure_pages(PAGE)
    names = ["Leaf 1 — Cindralok's message", "Leaf 2 — the purified page"]
    print("Text column %.2fin wide, %.2fin of vertical room per inside page.\n"
          % (fit.COLUMN_IN, fit.BUDGET_IN))
    problems = []
    for name, blocks in zip(names, pages):
        used = height(blocks)
        pct = used / fit.BUDGET_IN * 100
        flag = "OK"
        if pct > 100:
            flag, _ = "OVER", problems.append(name)
        elif pct > 90:
            flag, _ = "TIGHT", problems.append(name)
        print("%-5s %-32s %5.2fin  %5.1f%% of page  (%d blocks)"
              % (flag, name, used, pct, len(blocks)))
    if problems:
        print("\nNeeds attention: " + ", ".join(problems))
        return 1
    print("\nBoth leaves fit with room to spare.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
