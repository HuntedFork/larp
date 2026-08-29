# Mystery — Requirements & Decisions Log

*A living document. As decisions and requirements change, we record them here with the date/turn they changed.*

---

## 1. Overview

We are building a large **mystery** for the LARP players of **Chicken's Rest**. Players
earn **clues** and use them to solve the mystery. At the heart of the mystery is a
**logic puzzle** the players are never explicitly told they are solving.

## 2. Clue Physical Format

- A clue is a **full sheet of paper, folded in half and stapled shut**.
- Players can only see the **outside** without opening it.
- The **outside** carries only a small placeholder label (e.g. *"Clue 1"*). The
  **DO NOT OPEN** gates were dropped from every clue (see the change log, 2026-08-27) —
  the sole exception is **Clue 4**, whose outside reads *"DO NOT OPEN until you have
  assembled the bones of the saint."*
- The **inside** contains a **lore document** — a piece of in-world text from the world
  of Chicken's Rest.

## 3. Lore Document Requirements

- Each inside must read like a **genuine lore document**: it has an **author**, a voice,
  and possibly **annotations / marginalia**.
- The **actual puzzle clues** are rendered in **bold** so players know what to look for.
- The bolded clues must **NOT** be phrased in the stilted way logic-puzzle clues usually
  are. They must **flow naturally** with the surrounding prose.
- Players are **never told** they are solving a logic puzzle.

### Clue directionality rule (Entity ↔ Ingredient)

- **A clue may NEVER positively associate an entity with a specific ingredient** (e.g.
  "the Bear uses Bone Dust"). Such a clue hands over an answer cell with no deduction.
- **A clue MAY negatively dissociate an entity from a specific ingredient** (e.g. "the
  Bear will not touch the dream-flower"). Negatives only eliminate a cell, preserving the
  need for transitive deduction.
- Every entity's ingredient must be reached **through another axis** (learn its element,
  then the element→ingredient link). See `clue-outline.md`.


## 4. Puzzle Structure

- **6 entities**, **6 alchemical elements**, and **6 alchemical ingredients** — as
  **THREE INDEPENDENT AXES** (a classic three-grid logic puzzle). Players must recover the
  full alignment: which entity has which element AND which ingredient, and (as a hidden
  sub-puzzle) which element pairs with which ingredient.
- The three axes are independent to enable **transitive** clues (see `clue-outline.md`,
  which is the working source of truth for the clue design).
- The **intended** element↔ingredient pairing (a thing players must DISCOVER, not a
  handout) is:
  - Ghost Pepper ↔ **Fire**
  - Amaranth ↔ **Spirit**
  - Rock Salt ↔ **Earth**
  - Bone Dust ↔ **Body**
  - Vile Glomphidious ↔ **Water** *(inferred — pending confirmation)*
  - Dogwheat ↔ **Air** *(inferred — pending confirmation)*
- The **6 alchemical ingredients** are the six ingredients used by the potions
  (`docs/potions/data.json`): Dogwheat, Vile Glomphidious, Bone Dust, Ghost Pepper,
  Rock Salt, Amaranth.
- The **6 alchemical elements**: Fire, Water, Earth, Air, Spirit, Body.
- The **6 entities**:
  1. The Bear God — **Ursgrom** (recommended; see `gods.md`)
  2. The Fish God — **Uggglub** *(name LOCKED)*
  3. The Iron God — **Korrenvast** (recommended; see `gods.md`)
  4. **Nytheris** — God of madness (players do NOT know this)
  5. **Thistlebarrow** — returning from last year
  6. **Cindralok** — returning from last year (the fire serpent)



## 5. Continuity With Last Year

- Last year's puzzle (unformatted) lives in `../../lastyear.txt`.
- Established last year and must remain consistent:
  - **Nytheris** — "Pale Reflection / She-Who-Covets / Keeper of the Glass Veil";
    motive **envy**; weakness the **Ancient Mask**; associated with mirrors, still
    water, reflections; secretly connected to the plague of beastmen. **She drove the
    beastmen mad**; they were **cured when the Ancient Mask drove her influence from the
    land**. This is the subject of lore doc **D5** (see `clue-outline.md`).
  - **The Beastpeople are GOATS.** They do not always think like people (count in fives,
    trust smell over words, fear still water/reflections). D5 is written by one of them.

  - **Thistlebarrow** — "Lord of Horn and Branch"; a great stag; associated with
    antler, root, dawn-song / horn; motive **wonder/curiosity** (seeks the Codex of the
    heavens).
  - **Cindralok** — "Serpens Cinis"; a serpent "coiled of soot and ember," scales that
    "smolder when the moon wanes"; a **fire-breather**; bound only by **silver chains**.
    A puzzle entity this year (replaces Ashroot); firmly tied to **Fire**.
  - Other last-year denizens (may be referenced but are NOT puzzle entities this year):
    - **Ashroot** — "the Rootbinder"; bark-and-briar being; weakness iron; motive grief;
      dwells in the Heart. *(Was a candidate this year; replaced by Cindralok.)*
    - **Veydran** — bell-crow, fear, weak to Ashes of the First Fire.


## 6. Deliverables

All deliverables live in **`docs/mystery/`**, reachable from the root `index.html`.

- `Requirements.md` — this document (requirements + change log).
- `gods.md` — name suggestions & rationale for the three new gods.
- `outline.md` — the full puzzle design: the three sets, the intended solution grid, the
  list of clues, and the **sanity-check proof** that the puzzle is solvable and has a
  **unique** solution.
- `solution.md` — a clean, **printable** solution grid (for storytellers).
- `clue.md` — the clues in a printable, fold-ready format (outside gate + inside lore).
- `worklog.md` — running record of work and decisions.

## 7. Rendering / Site Conventions (observed)

- Root `index.html` links to each section folder.
- Text/prop docs live under a section folder in `files/*.md`, rendered by a
  `doc.html?file=<name>` viewer using `marked`.
- Bold in markdown (`**...**`) renders as bold — perfect for highlighting embedded clues.

---

## Change Log

- **2026-08-22** — Initial requirements captured. Confirmed the 6 alchemical ingredients
  from `docs/potions/data.json`. Folder created at `docs/mystery/`. Decided on the
  deliverables list above.
- **2026-08-22 (rev 2)** — Major structural correction:
  - **Elements are alchemical, not elemental, and are a FIXED property of each
    ingredient** (Ghost Pepper→Fire, Amaranth→Spirit, Rock Salt→Body given by user;
    Vile Glomphidious→Water, Dogwheat→Air, Bone Dust→Earth inferred, pending
    confirmation). The puzzle is therefore a single god↔ingredient bijection, with
    element derived. Element set is now Fire/Water/Earth/Air/Spirit/Body (was
    Fire/Water/Earth/Air/Ice/Storm).
  - **Fish God name LOCKED as "Uggglub."**
  - `outline.md` and `solution.md` rewritten to the new structure; uniqueness re-proved.
- **2026-08-22 (rev 3)** — Roster & assignment changes:
  - **Ashroot replaced by Cindralok** (last year's fire serpent). Cindralok is now a
    puzzle entity and is firmly **Fire / Ghost Pepper**; a clue (C1) must be **very
    explicit** that Cindralok is fire-based.
  - **Element legend swap corrected:** Rock Salt → **Earth**, Bone Dust → **Body**.
  - **Korrenvast (Iron)** is now **Earth / Rock Salt** (iron & ore both dug from the
    ground); **Ursgrom (Bear)** is now **Body / Bone Dust** (the great bodily beast).
    (Iron → Bone Dust was dropped as thematically weak.)
  - New intended solution: Ursgrom=Body/Bone Dust, Uggglub=Water/Vile Glomphidious,
    Korrenvast=Earth/Rock Salt, Nytheris=Spirit/Amaranth, Thistlebarrow=Air/Dogwheat,
    Cindralok=Fire/Ghost Pepper. Uniqueness re-proved in `outline.md` §4.
- **2026-08-22 (rev 4)** — Structure & clue-design overhaul:
  - **Puzzle is now THREE INDEPENDENT AXES** (Entity / Element / Ingredient), not a
    welded element=ingredient pair. This enables transitive clues. The element↔ingredient
    pairing becomes a hidden sub-puzzle players must solve.
  - **Clue directionality rule added:** positive Entity↔Ingredient clues are FORBIDDEN;
    negative Entity↔Ingredient clues are ALLOWED. (See §3.)
  - **New file `clue-outline.md`** is the working source of truth for clue design: solution
    grid + 12 raw transitive clues (1 explicit seed = Cindralok=Fire; no positive E–I) +
    uniqueness trace + plan mapping 12 clues into 6 lore docs (D1–D6). Linked in the index.
  - **TODO:** `outline.md` and `solution.md` still describe the older welded-axis model and
    must be reconciled to the 3-axis design (or retired in favor of `clue-outline.md`).
- **2026-08-27** — The Saint's Box revision:
  - **DO NOT OPEN gates removed from all clues except Clue 4.** Clue outsides are now plain
    "Clue N" labels (clues 9/10 keep their "PROPERTY OF THE LIBRARY" covers).
  - **Clue 4 rewritten** from *The Alchemist's Journal* to *The Bones of the Saint*: the
    cover reads *"DO NOT OPEN until you have assembled the bones of the saint."* Inside, the
    assembled skeleton rattles upright and **Saint Merewen** tells the story of her life,
    ending with her dying request that her crypt be dressed with **Amaranth, the Flower of
    the Spirit** — C5 (Spirit→Amaranth) is now delivered directly, not by elimination.
  - **New pointer clue (`clue11.html`):** *The Record of the Consecration of the Saint* —
    renowned for putting spirits at rest, both those in people and those that walked free;
    buried in Chicken's Rest **beneath the red tablecloth**. No grid clue; it leads players
    to the saint's box.
  - **New printable relic cards (`saint-cards.html`):** *Hand of the Saint* and *Foot of
    the Saint*, a quarter page each — rest the relic on someone, show the card, and they
    must tell you something that has been bothering them.
  - **Setup doc gains "The Saint's Box"** start-of-game setup: bones, 2× Bone Dust, Clue 4,
    the two relic cards, and the red tablecloth on top. (Deliberately NOT on the timeline.)
- **2026-08-28** — Clue distribution pinned; Clue Fragments retired:
  - **Clue Fragments removed from the game.** They were unredeemable (only 2 existed in the
    whole character deck, against a 3-fragment price) and the "NPC station" they referenced
    was never defined anywhere. Cut from the Alchemist and Scholar sheets and from the Print
    Checklist.
  - **The Scholar now starts with "a mysterious message"** — this is **Clue 5**
    (*A Letter on the River-God*), handed over with their sheet. It puts a real clue in a
    player's hands at minute one and gives the Scholar something to chase.
  - **Every clue now has exactly one assigned home** (see the Props Checklist table):
    1 → Rat Witch, 2 → Merchant Pack A, 3 → Merchant Pack B, 4 → the saint's box,
    5 → the Scholar, 6 → Second Shipment (3 coins), 7 → Cups, 8 → the beastmen (torn in
    half), 9 & 10 → Library setup, 11 → Pile o' Post 1. This closes the old §6 open
    decision ("which doc is easiest to earn"): the **load-bearing L–I clues 2 and 3 sit in
    the merchant packs**, the only source guaranteed to be in town from the first minute,
    and the survivable **Clue 8** is the one that gets torn in half and drunk away.
  - **Setup doc's broken "Library Setup" stub replaced** with a real section placing
    Clues 9 and 10 in the play area before game start.
  - **New `all-clues.html` — every clue in one print job.** Printing eleven separate pages
    was a chore, so this page collects all 11 clues in order: 22 pages = **11 double-sided
    sheets, one clue per sheet**. It does **not** copy the lore — it fetches `clue1.html` …
    `clue11.html` and lifts the two `.page` elements out of each, so it can never drift out
    of sync when a clue is edited. Each clue keeps its own cover, gate, and folding
    behaviour. On screen every sheet is captioned with its title and where the prop ends up
    (mirroring the Props Checklist table); those captions are `display:none` in print.
    *(Last year's clues were already a single combined document —
    `docs/docs/last-years-clues.html` — so no equivalent was needed there.)*



