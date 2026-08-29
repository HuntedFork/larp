# Mystery — Work Log

*Running record of work and decisions. Newest entries at the bottom.*

---

## 2026-08-22 — Kickoff & Outline Lock

**Done:**

- Created `docs/mystery/` folder, reachable from root `index.html`.
- Wrote `Requirements.md` (requirements + change log).
- Confirmed the **6 alchemical ingredients** from `docs/potions/data.json`:
  Dogwheat, Vile Glomphidious, Bone Dust, Ghost Pepper, Rock Salt, Amaranth.
- Wrote `gods.md` — name suggestions for the three new gods. Recommended set:
  - Bear God → **Ursgrom, the Slumbering Mountain**
  - Fish God → **Sethmara, the Drowned Choir**
  - Iron God → **Korrenvast, the Unbending**
- Wrote `outline.md` — the puzzle design bible: three sets, the intended solution grid,
  13 clues (10 load-bearing + 3 redundant confirmers), and a full **uniqueness proof**
  (§4 Sanity Check).
- Wrote `solution.md` — printable storyteller answer key with quick-reference lookups.

**Decisions locked (this phase):**

- Puzzle is a **three-set bijection** (entity ↔ element ↔ ingredient), 6×6×6.
- **Elements chosen:** Fire, Water, Earth, Air, Ice, Storm.
- **Intended solution:**
  - Ursgrom (Bear) = Earth / Rock Salt
  - Sethmara (Fish) = Water / Amaranth
  - Korrenvast (Iron) = Storm / Bone Dust
  - Nytheris = Ice / Ghost Pepper
  - Thistlebarrow = Air / Dogwheat
  - Ashroot = Fire / Vile Glomphidious
- **Uniqueness verified** by hand-trace in `outline.md` §4. Solution is forced.
- **Continuity with last year** preserved (Nytheris/envy/mask, Thistlebarrow/horn,
  Ashroot/grief/iron-weakness/fire). Ashroot=Fire deliberately matches her canon.

**Deferred (per direction):**

- **Clues (`clue.md`) NOT yet written.** Holding until the outline is signed off.
  The plain-logic clue statements (C1–C13) are recorded in `outline.md` §3 and ready to
  be dressed into lore documents when we resume.

**Next:**

- Get outline sign-off. Then write the lore-document clues in `clue.md`.

---

## 2026-08-22 — Rev 2: Alchemical Elements + Fish Name

**Feedback incorporated:**

- **Fish God renamed → Uggglub** (locked). Epithet still "the Drowned Choir" (working).
- **"Elements" are alchemical, not elemental, and are FIXED to the ingredient.** Given:
  Ghost Pepper→Fire, Amaranth→Spirit, Rock Salt→Body. Inferred (pending confirmation):
  Vile Glomphidious→Water, Dogwheat→Air, Bone Dust→Earth. Element set is now
  **Fire/Water/Earth/Air/Spirit/Body** (dropped Ice/Storm).

**Structural impact:** element is no longer a free third set — it's a property of the
ingredient. The puzzle collapses to a **single god↔ingredient bijection** (6×6), with
element read off the fixed legend. Clues can speak in element OR ingredient terms.

**Revised solution (re-proved unique in `outline.md` §4):**

- Ursgrom (Bear) = Bone Dust / Earth
- Uggglub (Fish) = Vile Glomphidious / Water
- Korrenvast (Iron) = Rock Salt / Body
- Nytheris = Amaranth / Spirit  *(Spirit = the hollowing of the self — thematic bullseye)*
- Thistlebarrow = Dogwheat / Air
- Ashroot = Ghost Pepper / Fire  *(matches last-year canon)*

**Files updated:** `gods.md`, `outline.md`, `solution.md`, `Requirements.md` (change log),
this `worklog.md`.

**Still open:** confirm the 3 inferred ingredient→element mappings; pick Fish epithet and
final Bear/Iron names. Clues (`clue.md`) still deferred until outline sign-off.

---

## 2026-08-22 — Rev 3: Cindralok In, Bear/Iron Swap

**Feedback incorporated:**

- **Ashroot → Cindralok** (last year's fire serpent — a far better Fire fit). Cindralok is
  now the Fire / Ghost Pepper entity. **Clue C1 is flagged to be *very explicit*** that
  Cindralok is a fire-breathing creature (serpent of soot and ember).
- **Element legend corrected** to Rock Salt = **Earth**, Bone Dust = **Body**.
- **Korrenvast (Iron)** now = **Earth / Rock Salt** (iron and ore are dug from the same
  ground; "Iron → Bone Dust" was thematically weak and is dropped).
- **Ursgrom (Bear)** now = **Body / Bone Dust** (the great bodily beast; the sleeping
  *body* of the mountain).

**Current locked solution (re-proved unique in `outline.md` §4):**

- Ursgrom (Bear) = Bone Dust / Body
- Uggglub (Fish) = Vile Glomphidious / Water
- Korrenvast (Iron) = Rock Salt / Earth
- Nytheris = Amaranth / Spirit
- Thistlebarrow = Dogwheat / Air
- Cindralok = Ghost Pepper / Fire  *(explicit fire clue required — C1)*

**Files updated:** `outline.md`, `solution.md`, `Requirements.md` (entities, legend,
continuity, change log rev 3), this `worklog.md`.

**Still open:** confirm the 2 remaining inferred mappings (Vile Glomphidious→Water,
Dogwheat→Air); pick Fish epithet + final Bear/Iron names. Clues (`clue.md`) still deferred
until outline sign-off — note the standing requirement that **C1 be explicit about
Cindralok = Fire**.

---

## 2026-08-22 — Rev 4: Three Independent Axes + Transitive Clue Outline

**Big design shift (per discussion):** the puzzle is now **three genuinely independent
axes** — Entity, Element, Ingredient — instead of element being welded to ingredient. This
was the user's original intent and it makes **transitive** clues natural.

**Design goals locked:**
- Maximize **transitive** deduction; **no clue maps an Entity directly to an Ingredient**.
- Exactly **one explicit seed**: Cindralok = Fire.
- Entities resolve in **~2 hops** (moderate). L–I "reagent of each element" clues are the
  transitivity glue.
- Keep **document count ≈ 6** to match last year. Chose **3 axes over 4** after clue-count
  math (4 axes would need ~17 clues / denser docs); 3 axes ≈ 12 clues fits ~6 docs @ 2 each.

**New file:** `clue-outline.md` — contains the solution grid, all 12 raw logical clues
(tagged E–L / E–I / L–I), a transitive solve trace proving uniqueness, and a plan mapping
the 12 clues into **6 lore documents** (D1–D6). Linked into the mystery index.

**Note:** `outline.md` / `solution.md` still describe the *older* welded-axis version; they
should be reconciled to the 3-axis model once this clue outline is signed off (or we treat
`clue-outline.md` as the new source of truth going forward).

**Deferred:** writing the actual lore prose in `clue.md` until the clue outline is approved.

---

## 2026-08-22 — Rev 5: Goat-Kin Doc + 8 Documents

**Feedback incorporated:**

- **D5 → "The Goat-Kin's Record of the Madness."** Rewrote the old "Madwoman's Confession"
  as a first-person account **by a beastperson (goat)**: how **Nytheris drove the beastmen
  mad** and how they were **cured when the Ancient Mask drove her from the land**. Carries
  C9 (Nytheris=Spirit) and C10 (Bear=Body / stag≠Body), the latter folded in as a
  **prayer of protection against Nytheris's return**. Unsettling, not-quite-human voice.
  Beastpeople are GOATS (recorded in `Requirements.md` §5).
- **Document count 6 → 8.** Split the crammed 3-clue ledger into **three ledger pages**
  (D2/D3/D4) and split the river/iron letter into **two docs** (D5 Fish, D6 Iron). New
  layout D1–D8; each doc now carries only 1–2 clues. Goat-kin doc is now **D7**, stag
  verse **D8**. All 12 clues still placed; nothing else about the puzzle changed.

**File updated:** `clue-outline.md` (§5 doc plan, density & redundancy notes).

**Still deferred:** writing the actual lore prose in `clue.md`.

---

## 2026-08-25 — Iron God Rewritten as a God of Fortune

**Change:** Korrenvast is no longer a god of discipline and toil. He is now a **god of
fortune** who carries a **great iron coin** (his god icon) and flips it to settle
everything. Epithet changed from *"the Unbending"* to **"the Turning Coin."**

- **New belief:** magic should be **distributed at random** — not to the studied, the
  pious, or the hard-working, but to whoever the coin lands on. The **iron veins** are his
  proof: ore is scattered blind through the deep stone and goes to the **bold and
  fortunate** miner, not the diligent one.
- **New power — *Fortune's Favor*:** each hour take **10 coins from the box**, usable
  ONLY for bets with other players; each bet is **something they own vs. his coins**,
  decided by a **flip of the god icon**. (Replaces *Reward of Labor*.)
- **Puzzle unaffected:** Korrenvast is still **Earth / Rock Salt**; clue **C8/D6** still
  reads "the Iron God holds the Earth." `clue6.html` (*The Forge-Warden's Testament*) was
  re-flavoured to random, luck-struck seams while keeping the bolded load-bearing line
  intact.

**Files updated:** `docs/docs/files/gods.md` (Korrenvast page + the Bear's and River's
opinions of him), `docs/docs/files/setup.md`, `docs/docs/files/props-checklist.md` (great
iron coin added as a prop; coin box stocked for 10/hour), `docs/mods/files/ghost-invasion.md`
(madman's name list), `docs/mystery/gods.md`, `docs/mystery/outline.md`,
`docs/mystery/clue6.html`.

---

## 2026-08-27 — The Saint's Box

**Changes (per direction):**

- **Gates removed.** The DO NOT OPEN cover is gone from every clue except **Clue 4**
  (`clue1–3`, `clue5–8` now have plain "Clue N" covers; clues 9/10 keep "PROPERTY OF THE
  LIBRARY"). `Requirements.md` §2 updated.
- **Clue 4 rewritten** as *The Bones of the Saint* (was *The Alchemist's Journal*). Its
  cover is the one remaining gate: *"DO NOT OPEN until you have assembled the bones of the
  saint."* Inside: as the last dusty bone slots into place the skeleton rattles, sits up,
  and speaks — **Saint Merewen** tells her life story and ends by asking that her crypt be
  decorated with **Amaranth, the Flower of the Spirit**. The puzzle fact is unchanged
  (C5: Spirit→Amaranth) but is now delivered **directly** instead of by elimination, so D4
  no longer depends on D2+D3. Her one admitted failure — the great hollowing of the
  beast-kin, which took the Mask to end — nods to last year without naming Nytheris.
- **New Clue 11** — *The Record of the Consecration of the Saint*: a chapel record naming
  her renown (she put spirits at rest, **both those in people and those that walked
  free**) and her grave: **buried in Chicken's Rest, beneath the red tablecloth**. It
  carries no grid clue; it points players to the saint's box.
- **New printable `saint-cards.html`** — *Hand of the Saint* / *Foot of the Saint* relic
  cards (a quarter page each, bone/sepia theme, one of each): rest the relic on someone,
  show the card, and they must tell you something that has been bothering them.
- **Setup doc** gains a "The Saint's Box" section (bones, 2× Bone Dust, Clue 4, the two
  relic cards, red tablecloth on top); **props checklist** gains the box, the red
  tablecloth, and the cards. Kept out of the timeline on purpose — the box is a
  start-of-game setup step, not a scheduled event.

**Files updated:** `clue1–8.html`, `clue4.html` (rewrite), `clue11.html` (new),
`saint-cards.html` + `saint-cards-print.css` (new), `clue-print.css`, `clue1-print.css`,
`index.html`, `clue-outline.md`, `Requirements.md`, `files/d1-bestiary-of-the-heart.md`,
`docs/docs/files/setup.md`, `docs/docs/files/props-checklist.md`.

---

## 2026-08-28 — Clue Fragments retired, distribution pinned, print consolidation

- **Clue Fragments cut from the game.** Unredeemable as written (2 in the whole deck vs. a
  3-fragment price) and the "NPC station" was never a real place. Removed from the
  Alchemist and Scholar.
- **The Scholar now starts with "a mysterious message"** = **Clue 5** (*A Letter on the
  River-God*). A real clue in a player's hands from minute one.
- **Every clue pinned to exactly one home** — full table in the Props Checklist. The
  load-bearing L–I clues (2, 3) went to the merchant packs, the only guaranteed early
  source; the survivable Clue 8 is the one torn in half for the beastmen. This closes the
  old `clue-outline.md` §6 question of which document should be easiest to earn.
- **New `all-clues.html`** — all 11 of this year's clues in one print job (11 double-sided
  sheets, one clue per sheet). It fetches the individual `clueN.html` files and lifts their
  `.page` elements rather than copying the lore, so it cannot fall out of sync.
- **Last year's clues de-gated.** The ten *DO NOT OPEN* covers and their opening conditions
  (Truth Seeker rituals, symposiums, chants) are replaced by a single archivist's stamp:
  **"Chicken's Rest Historical Document — Accuracy Unknown."** They are now readable town
  records of uncertain truth, which also sets up nicely against this year's documents. The
  storyteller solution page keeps its *STORYTELLERS ONLY* header.

**Files updated:** `docs/characters/data.json`, `docs/mystery/all-clues.html` (new),
`docs/mystery/index.html`, `print-checklist.html`, `docs/docs/files/props-checklist.md`,
`docs/docs/files/setup.md`, `docs/docs/files/timeline.md`, `docs/docs/pile-of-post.html`,
`docs/docs/last-years-clues.html` + `-print.css`, `docs/docs/index.html`,
`docs/mods/files/{rat-witch,cups,beastmen-come-to-town,shipments}.md`, `Requirements.md`.


---

## 2026-08-28 — The clues get a period typeface

The clues are meant to read as documents found in the world — a bestiary, a cook's recipe,
a magistrate's ruling — but they were set in Georgia, the same face as every design doc in
the repo. They now have type that matches what they are.

- **Three faces, self-hosted** in `docs/shared/fonts/` and declared by the new
  `docs/shared/fonts.css`:
  - **EB Garamond** for body text — an old-style book serif, the look of a printed page of
    the period.
  - **Cinzel** for headings and the cover stamps (*Clue N*, *DO NOT OPEN*, *PROPERTY OF THE
    LIBRARY*) — Roman inscriptional capitals, so a stamp reads as carved or struck rather
    than typed.
  - **Caveat** for the marginalia. The margin notes are written *by a later hand* — that is
    the fiction — so they are now in a hand instead of small italics, and read as scribbled
    into the document rather than typeset with it.
- **Self-hosted on purpose.** The files are in the repo, not fetched from a font CDN, so the
  props print the same on the GM's laptop with no network at print time. Every stack falls
  back to Georgia, so a missing file degrades to the old look instead of breaking the sheet.
- **Body size raised 10.5pt → 11.5pt** (line-height 1.4 → 1.3). Garamond has a notably
  smaller x-height than Georgia, so at the old size it would have printed visibly smaller;
  the larger size keeps the same apparent size on paper. Marginalia went 8.5pt → 11pt for
  the same reason — Caveat is a small, light hand.
- **`DO NOT OPEN` 40pt → 34pt** and `PROPERTY OF THE LIBRARY` 30pt → 26pt: Cinzel is a much
  wider face than Georgia, and at the old sizes the stamps ran to the edge of the sheet.
- **Saint relic cards** were brought along, since they live in the saint's box beside
  Clue 4 and would otherwise be the odd prop out.

**New `tools/check-clue-fit.py`.** The inside page of a clue is a fixed-height box with
`overflow: hidden` — text that outgrows it is silently cut off *on paper* while still
looking correct in the browser, which is exactly the failure this project can least afford.
The script reads the real advance widths out of the woff2 files (including the true bold
widths, since the puzzle facts are all in `<strong>`), wraps every clue, and reports how
full each page is. Clue 1 is the fullest at **88.4%**; all eleven fit.

**Files updated:** `docs/shared/fonts.css` + `docs/shared/fonts/*.woff2` (new),
`docs/mystery/clue-print.css`, `docs/mystery/clue1-print.css`,
`docs/mystery/saint-cards-print.css`, `tools/check-clue-fit.py` (new), `AGENT.md`.

---

## 2026-08-28 (later) — The documents are handwritten, so set them in hand

The first pass only put the *marginalia* in a hand and left the document body in Garamond,
which was half a job: the clues say outright what they are — a cook's receipt *"in a broad,
confident hand"*, a pilgrim's letter, a leaf *"in a hand none of the town can name"* — so a
typeset body was contradicting the frontispiece on the same page.

- **Body is now Kalam** (10.5pt/1.42). Kalam's x-height is ~30% larger than Garamond's, so
  10.5pt prints about as large as the 11.5pt serif did — the point size went *down* while
  the apparent size stayed put. Leading was opened to 1.42 because a hand needs more air
  between lines than a serif.
- **Kalam has a real bold**, which was the deciding factor: every puzzle fact in the mystery
  is in `<strong>`, and a hand without a bold weight would have flattened the one piece of
  formatting the puzzle depends on. Architects Daughter reads better as a body face but has
  no bold, which is why it did not get the job.
- **Two different hands, on purpose.** Marginalia moved to **Architects Daughter**. The
  clues describe the margin notes as *"a different, shakier hand below"* and *"a reader's
  note in pencil"* — same-font-but-smaller would have read as the author annotating himself.
  It now reads as pencil against ink.
- **Cinzel stays** for headings and cover stamps, which are stamped/carved rather than
  written, and **EB Garamond is kept** as the new `--font-printed` role.
- **Saint relic cards moved to `--font-printed`.** They are rules text you show a player,
  not a handwritten artifact, so they should not be in a hand.

**Fit tool fixed while doing this.** Kalam is a static family (one file per weight), not a
variable font, so the bold-instancing path silently measured bold text at regular width. The
tool now maps a static family to its real bold file — bold measures 5% wider, as it should.
Without the fix the estimate would have been quietly optimistic, which is the one thing a
fit checker must not be. Clue 1 remains the fullest page at **88.1%**; all eleven fit.

**`docs/mystery/hand-specimen.html` (new, screen-only).** A comparison sheet: the body in
Kalam / Patrick Hand / Architects Daughter / Garamond, then the margin hands, all set with
real clue text at true print size. It is a working document for choosing type — not a prop,
and deliberately not on the print checklist. Delete it once the choice is settled.

**Files updated:** `docs/shared/fonts.css`, `docs/shared/fonts/kalam-*.woff2` +
`architectsdaughter-latin.woff2` (new), `docs/mystery/clue-print.css`,
`docs/mystery/clue1-print.css`, `docs/mystery/saint-cards-print.css`,
`docs/mystery/hand-specimen.html` (new), `tools/check-clue-fit.py`, `AGENT.md`.
