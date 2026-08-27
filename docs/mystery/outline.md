# Mystery — Puzzle Outline, Solution Grid & Sanity Proof

*This is the design bible for the logic puzzle. Storyteller-facing. Never shown to
players. The player-facing versions of these clues (embedded in lore, bolded) live in
`clue.md`.*

---

## 0. IMPORTANT — How the "Elements" Work

The six "elements" are **alchemical**, not the classic elemental wheel, and they are a
**fixed property of each alchemical ingredient** — not a free third set. The ingredient
determines the element:

| Ingredient | Alchemical Element |
|------------|--------------------|
| Ghost Pepper | **Fire** *(given)* |
| Amaranth | **Spirit** *(given)* |
| Rock Salt | **Earth** *(the mineral of the ground)* |
| Bone Dust | **Body** *(bone is the body's frame — the reagent of flesh & structure)* |
| Vile Glomphidious | **Water** *(inferred — the vile fluid/dissolving reagent)* |
| Dogwheat | **Air** *(inferred — wind-borne grain, the breath/charm reagent)* |

> **The two inferred mappings (Water, Air) are provisional — flag any you want changed and
> it ripples cleanly through the rest of the design.**

**Structural consequence:** because element is locked to ingredient, the puzzle is really
a **single bijection — the 6 gods matched to the 6 ingredients.** Each god's element is
then read off the table above. This is *good*: clues may speak in terms of **element** or
**ingredient** interchangeably (they carry the same information), which gives us lots of
natural ways to phrase lore without sounding like a logic grid.

---

## 1. The Two Sets (plus derived element)

**Entities (6)** — the gods of the Heart:

1. Ursgrom (the Bear God)
2. Uggglub (the Fish God)
3. Korrenvast (the Iron God)
4. Nytheris (secretly the god of madness)
5. Thistlebarrow (returning)
6. Cindralok (returning — the fire serpent)

**Alchemical Ingredients (6)** — from `docs/potions/data.json`, each with its fixed
element:

1. Dogwheat *(Air)*
2. Vile Glomphidious *(Water)*
3. Bone Dust *(Body)*
4. Ghost Pepper *(Fire)*
5. Rock Salt *(Earth)*
6. Amaranth *(Spirit)*

The players must recover **which god goes with which ingredient** (and therefore which
element).

---

## 2. The Intended Solution

| Entity | Ingredient | Element (derived) |
|--------|------------|-------------------|
| **Ursgrom** (Bear) | Bone Dust | Body |
| **Uggglub** (Fish) | Vile Glomphidious | Water |
| **Korrenvast** (Iron) | Rock Salt | Earth |
| **Nytheris** | Amaranth | Spirit |
| **Thistlebarrow** | Dogwheat | Air |
| **Cindralok** | Ghost Pepper | Fire |

### Design rationale (why these pairings feel "true")

- **Cindralok → Ghost Pepper (Fire).** Canon from last year: "a serpent coiled of soot and
  ember," scales that "smolder when the moon wanes," a fire-breather bound only by silver
  chains. Fire is unambiguously his, and Ghost Pepper is the fire reagent. This is the
  cleanest pairing in the puzzle — we lean into it with an explicit clue (C1).
- **Uggglub (Fish) → Vile Glomphidious (Water).** The Drowned Choir of the river; Vile
  Glomphidious is the watery, fishy fluid reagent (Fish Oil, Moon Oil). Perfect fit.
- **Korrenvast (Iron) → Rock Salt (Earth).** The Turning Coin, drawn from ore in the deep
  ground; Rock Salt is the literal mineral of the earth, mined from stone. Iron and Earth
  are kin — both dug from the mountain's bones.
- **Ursgrom (Bear) → Bone Dust (Body).** The Slumbering Mountain of muscle and hide; the
  great bodily beast. Bone Dust is the reagent of the frame — flesh, sinew, and skeleton —
  and a hibernating bear is the very picture of the sleeping *body*.
- **Nytheris → Amaranth (Spirit).** She hollows the *spirit* — steals reflections,
  courage, song, the soul's inner things. Spirit is the element of the god of madness who
  unmakes the self. Amaranth (the "borrowed dreams" / soul reagent) fits her theft of
  identity.
- **Thistlebarrow → Dogwheat (Air).** The stag of horn and branch; his dawn-song / horn
  rides the wind, antlers to the sky. Dogwheat is the airy, wind-borne grain and the
  charm/suggestion reagent (the persuasive breath of the herald).

---

## 3. The Clues (storyteller-plain form)

Because element ≡ ingredient, each clue can be phrased either way in lore. Below are the
logical statements. Numbered C1–C12 (load-bearing marked ★; redundant confirmers marked
◇). A god is pinned as soon as we know **either** its ingredient **or** its element.

- **C1 ★** Cindralok's power is **Fire** (⇒ Ghost Pepper). *This clue must be **very
  explicit** — the lore doc for C1 should state plainly and unmistakably that Cindralok is
  a creature of fire (fire-breathing serpent of soot and ember). No subtlety here.*
- **C2 ★** The Fish God's reagent is **Vile Glomphidious** (⇒ Water).
- **C3 ★** The Iron God's element is **Earth** (⇒ Rock Salt).
- **C4 ★** Nytheris is bound to **Spirit** (⇒ Amaranth) — she preys on the soul itself.
- **C5 ★** The Bear God's reagent is **Bone Dust** (⇒ Body).
  *(C1–C5 pin five gods; the sixth, Thistlebarrow, must take the remaining reagent
  Dogwheat / Air.)*
- **C6 ◇** Thistlebarrow's song rides the **Air** (⇒ Dogwheat). *(redundant confirmer)*

Redundant "shape of the negative" confirmers (help groups that miss a load-bearing clue,
and reinforce the lore):

- **C7 ◇** Nytheris is **not** a creature of Fire — cold, not flame, follows her. (¬Fire)
- **C8 ◇** The Bear God has no part in **Spirit-work**; his gift is of blood and bone.
  (Bear ≠ Amaranth)
- **C9 ◇** Cindralok is **not** a being of the deep **Earth** — his realm is ember and
  ash, not stone (Rock Salt is not his). (Cindralok ≠ Rock Salt)
- **C10 ◇** The Fish God is **not** of the Air. (Fish ≠ Dogwheat)
- **C11 ◇** The Iron God is **not** a being of **Fire** (though iron glows in the forge,
  the flame is Cindralok's, not his). (Iron ≠ Ghost Pepper)
- **C12 ◇** Thistlebarrow's reagent is **not Bone Dust** (Body is the Bear's, not the
  stag's). (Thistlebarrow ≠ Bone Dust)

> **Minimal forcing set:** {C1, C2, C3, C4, C5}. Five direct anchors pin five gods; the
> last god (Thistlebarrow) is forced to the leftover reagent by elimination. C6–C12 are
> all redundant confirmers for robustness and flavor — deploy as many as you like.

---

## 4. Sanity Check — Proof of a Unique Solution

Gods: Bear (Ursgrom), Fish (Uggglub), Iron (Korrenvast), Nytheris, Thistlebarrow,
Cindralok. Reagents (with fixed element): Ghost Pepper/Fire, Vile Glomphidious/Water, Bone
Dust/Body, Rock Salt/Earth, Amaranth/Spirit, Dogwheat/Air.

It suffices to solve the god↔reagent bijection; element then follows from the fixed table.

Apply the five direct anchors:

- C1: Cindralok = Fire = **Ghost Pepper**.
- C2: Fish (Uggglub) = **Vile Glomphidious** (Water).
- C3: Iron (Korrenvast) = Earth = **Rock Salt**.
- C4: Nytheris = Spirit = **Amaranth**.
- C5: Bear (Ursgrom) = **Bone Dust** (Body).

Five gods now hold five distinct reagents: Ghost Pepper, Vile Glomphidious, Rock Salt,
Amaranth, Bone Dust. The only god left is **Thistlebarrow**, and the only reagent left is
**Dogwheat** (Air). Therefore Thistlebarrow = **Dogwheat / Air**. ✔

Every assignment is forced; no reagent is used twice; the leftover is unique. Hence the
solution is **unique and solvable**. The redundant confirmers C6–C12 are each consistent
with this assignment (spot-check: C7 ¬Fire for Nytheris ✔ since she's Spirit; C12
Thistlebarrow ≠ Bone Dust ✔ since he's Dogwheat; etc.). ∎

### 4a. Robustness / difficulty notes

- **Every one of C1–C5 is load-bearing.** Drop any single one and its god plus
  Thistlebarrow become mutually ambiguous over two leftover reagents — the final
  elimination fails. That's why we ship the C6–C12 confirmers: a group that never earns,
  say, C4 can still recover Nytheris = Spirit from C7 (¬Fire) combined with the other
  anchors narrowing the field.
- **Difficulty knob (harder):** replace a direct anchor with a pure chain of negatives
  (e.g. drop C3 and rely on C9 + C11 + elimination to force the Iron God to Earth). Still
  unique, more chaining required. Logged as an option; not applied.
- **Difficulty knob (easier):** because element ≡ ingredient, we can seed the players with
  the ingredient→element legend (§0 table) as a "found alchemist's notes" prop so they
  realize the two are the same axis. Recommended for a first-time group.

---

## 5. Open Questions / To Decide

- **Confirm the 2 inferred ingredient→element mappings** (Vile Glomphidious→Water,
  Dogwheat→Air). Everything downstream depends on these.
- Fish God epithet (name **Uggglub** is locked; epithet options in `gods.md`).
- Final Bear/Iron god names (recommended set in `gods.md`).
- How clues are **earned** in play (gating conditions in last-year style) — for `clue.md`.
- Whether to hand players the §0 ingredient→element legend as an in-world prop.
