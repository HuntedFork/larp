# AGENT.md

Guidance for AI agents (and humans) working in this LARP reference repo.

## Project shape

This is a static site of LARP reference material. No build step — everything is plain
HTML/CSS/JS opened directly in a browser.

- **Section index pages** live at `docs/<section>/index.html` and are linked from the root
  `index.html`.
- **Long-form documents** (mods, indymods, docs, rituals) are Markdown files under
  `docs/<section>/files/*.md`, rendered by a small loader page (e.g. `mod.html?file=<name>`,
  `doc.html?file=<name>`) using `marked`. Each loader has a matching `*-print.css`.
- **Card decks** (potions, mishaps, curses, characters) are `data.json` + `index.html` that
  use `docs/shared/card-renderer.js` and `docs/shared/print.css`.

When you add a new document, always **link it from the relevant section `index.html`**.

## Mods vs. IndyMods

- **Mods** (`docs/mods/`) are scheduled encounters that run at a set time during the game.
- **IndyMods** (`docs/indymods/`) are independent, run-them-whenever encounters. They are
  NOT scheduled.

## The Game Timeline — `docs/docs/files/timeline.md`

This is the schedule the GM prints and follows while running the game. Keep it correct
whenever mods or shipments change.

**Rules for the timeline:**

1. **Runs 11:30 AM – 5:00 PM**, in **half-hour slots** (11:30, 12:00, 12:30, … 5:00).
2. **Start times only** — list when each event *begins*, not its duration.
3. **Fixed anchors:** 11:30 = Setup, 12:00 = Game Start, 5:00 = Game End. Don't move these.
4. **Include every regular *mod*** (from `docs/mods/`) plus the **First Shipment** and
   **Second Shipment**.
5. **Do NOT put IndyMods on the timeline** — they run ad-hoc.
6. **Two events may share a half-hour slot** — list them as duplicate time entries. There are
   **two game runners** and each mod needs 1 or 2; every slot should keep both runners in use
   (pair two 1-runner mods, or run one 2-runner mod alone).
7. **Spread events out evenly** across the day rather than clustering them.
8. Leave unused slots marked `*(open)*` so it's obvious where new mods can go, and update
   the "Open Slots" note at the bottom.

**When adding a new mod:** write the mod under `docs/mods/files/`, link it from
`docs/mods/index.html`, **add it to the `SECTIONS` list in `docs/mods/all-mods.html`**, then
place it in an open, evenly-spaced timeline slot — re-balancing the movable events if needed
to keep the spacing even and the no-shared-slot rule intact.

## Combined "print everything" pages

Some sections have a page that gathers every document in that section into one print job, so
the GM isn't opening a dozen tabs:

- `docs/mods/all-mods.html` — every **mod and IndyMod** (single-sided, one per sheet).
- `docs/mystery/all-clues.html` — every **clue** (double-sided, one clue per sheet).

These pages **fetch the source files at load time and never copy their content**, so they
cannot fall out of sync — but each keeps an explicit ordered list of filenames.

**Rule:** when you add a mod, IndyMod, or clue, add its filename to the corresponding list
(`SECTIONS` in `all-mods.html`, `CLUES` in `all-clues.html`). A document missing from the list
loads nowhere and silently never prints. Both pages must be **served over http** (local server
or the published site), not opened from a `file://` path — the same as every other loader.

## The Props Checklist — `docs/docs/files/props-checklist.md`

This is the master list of physical props the GM needs to run the game. It is organized by
prop *kind* (Coins, Ingredient Tags, Costume & Marker Props, Mod-Specific Props, Boxes,
Character Starting Props, Paper Props, Ritual Copies, Stations & Vessels).

**Rule:** Any time a mod, character, doc, or ritual specifies a **physical prop**, add it to
the Props Checklist (if it isn't already there), and always record **where it exists** — the
mod, character, or box it comes from. Every entry is a `- [ ]` checkbox with a *Where:* note.
The Coins and Ingredient Tags sections are counted tables; update the counts if you change a
purse or a shipment list.

## The Print Checklist — `print-checklist.html`

An index of hyperlinks to **every document in the project**, grouped the way you'd print them
(GM docs, characters, card decks, rituals, mods, indymods, docs printables, mystery), each
with a checkbox and a short print note.

**Rule:** When you add a new document anywhere, add it to the Print Checklist as well as the
relevant section `index.html`. Markdown docs are linked via their loader
(`doc.html?file=<name>`, `mod.html?file=<name>`, etc.), not by their `.md` path.

## Fonts on the printed props — `docs/shared/fonts.css`

The mystery clues (and the saint's relic cards) are **handwritten artifacts in the fiction** —
a cook's receipt "in a broad, confident hand", a pilgrim's letter, a leaf "in a hand none of
the town can name" — so they are set in hands, not in a book serif. The fonts are
**self-hosted** in `docs/shared/fonts/*.woff2` — not pulled from a font CDN — so a prop
prints identically whether or not the GM's machine has a network connection at print time.

`docs/shared/fonts.css` declares the `@font-face` rules and exposes four **role** variables.
Ask for the role, not the font name:

| Variable | Face | Used for |
| --- | --- | --- |
| `--font-book` | Kalam | the document body — the author's own hand |
| `--font-hand` | Architects Daughter | marginalia — a *different, later* reader's hand |
| `--font-inscription` | Cinzel | headings, cover stamps, card names |
| `--font-printed` | EB Garamond | anything genuinely printed rather than written |

The two hands are deliberately different faces: the clues say things like "a different,
shakier hand below", so a margin note must not look like the same person wrote it. Kalam
carries a real bold, which matters — every puzzle fact is in `<strong>` and has to stand out.

Every variable ends in a stack that falls back to a font on every machine, so a missing font
file degrades gracefully instead of breaking the prop. To use them, add
`@import url('../shared/fonts.css');` at the top of the stylesheet.

**Rule:** the clue inside-pages are fixed-height boxes with `overflow: hidden` — text that
outgrows one is *silently clipped* on the printed sheet and looks fine in the browser. After
changing clue type, spacing, or text, run:

```
python3 tools/check-clue-fit.py
```

It measures every clue with the real font metrics and fails if any page is over ~90% full.

The Cursed Tome's two folded leaves (`docs/docs/cursed-tome.html`) are the same kind of
fixed-height, `overflow: hidden` box, so they have their own check — it reuses the clue
measurer with the tome's block styles:

```
python3 tools/check-tome-fit.py
```

## Style conventions

- **Printables are judged by the printed page, nothing else.** If something looks wrong on
  paper — a stray heading, a screen-only note, a rule that pushes content down — cut it,
  even if it reads fine in the browser. Never add on-screen furniture to a document that
  gets handed to a player.
- Markdown docs *may* open with a single `# Title` (the loaders use the first `<h1>` for
  the page `<title>` when one exists, and fall back to a generic title when it doesn't).
  It is **not required** — omit it on anything meant to be printed and handed out.
- Match the tone of existing files: earthy, slightly archaic, evocative.
- Printable card sheets: keep the purple curse theme / existing card CSS patterns.
- Reference the shipments' contents in `docs/docs/files/setup.md`.

