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




