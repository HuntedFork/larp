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
6. **No two events may share the same half-hour slot.**
7. **Spread events out evenly** across the day rather than clustering them.
8. Leave unused slots marked `*(open)*` so it's obvious where new mods can go, and update
   the "Open Slots" note at the bottom.

**When adding a new mod:** write the mod under `docs/mods/files/`, link it from
`docs/mods/index.html`, then place it in an open, evenly-spaced timeline slot — re-balancing
the movable events if needed to keep the spacing even and the no-shared-slot rule intact.

## The Props Checklist — `docs/docs/files/props-checklist.md`

This is the master list of physical props the GM needs to run the game.

**Rule:** Any time a mod, character, doc, or anything else specifies a **physical prop**,
add it to the Props Checklist (if it isn't already there). Known physical props so far
include **coins**, **bones**, and **blue/green wristbands** (plus white headbands and the
optional magic ring). Keep this list current whenever you introduce a new prop.

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

