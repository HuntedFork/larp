# Mystery — Clue Outline (pre-writing plan)

*Storyteller-facing planning doc. This is the bridge between the puzzle design
(`outline.md`) and the finished lore documents (`clue.md`, to be written later). It holds:
(1) the solution grid, (2) the raw logical clues, (3) the planned lore documents and which
clues live in each. **No lore prose yet** — that comes after this is signed off.*

---

## 1. Structure recap (3 independent axes)

The puzzle has **three independent axes**. Players must recover the full alignment.

- **Entity:** Cindralok, Uggglub (Fish), Korrenvast (Iron), Thistlebarrow, Nytheris,
  Ursgrom (Bear)
- **Element:** Fire, Water, Earth, Air, Spirit, Body
- **Ingredient:** Ghost Pepper, Vile Glomphidious, Rock Salt, Dogwheat, Amaranth, Bone Dust

Clues link **pairs** of axes:
- **E–L** = Entity ↔ Element
- **E–I** = Entity ↔ Ingredient
- **L–I** = Element ↔ Ingredient

### Design rules (IMPORTANT)

- **No POSITIVE Entity↔Ingredient clue is ever allowed.** A clue may never state that an
  entity **IS** associated with a particular ingredient (e.g. "the Bear uses Bone Dust").
  Those hand over an answer cell with zero deduction.
- **NEGATIVE Entity↔Ingredient clues ARE allowed.** A clue may state that an entity is
  **NOT** associated with a particular ingredient (e.g. "the Bear will not touch the
  dream-flower"). Those only *eliminate* a cell, so the ingredient must still be reached
  transitively.
- An entity's ingredient is therefore always reached **through another axis**: learn its
  **element** (an E–L clue), then apply the matching **L–I** clue. ~2 hops.
- Exactly **one explicit seed**: Cindralok = Fire (E–L). Everything else is relational,
  element-based, or negative.


---

## 2. Solution Grid

| Entity | Element | Ingredient |
|--------|---------|------------|
| **Cindralok** | Fire | Ghost Pepper |
| **Uggglub** (Fish) | Water | Vile Glomphidious |
| **Korrenvast** (Iron) | Earth | Rock Salt |
| **Thistlebarrow** | Air | Dogwheat |
| **Nytheris** | Spirit | Amaranth |
| **Ursgrom** (Bear) | Body | Bone Dust |

### The hidden Element↔Ingredient sub-solution (players must also find this)
| Element | Ingredient |
|---------|------------|
| Fire | Ghost Pepper |
| Water | Vile Glomphidious |
| Earth | Rock Salt |
| Air | Dogwheat |
| Spirit | Amaranth |
| Body | Bone Dust |

---

## 3. Raw Logical Clues

Tagged by axis-pair. ★ = load-bearing, ◇ = redundant confirmer / robustness. "Hops" notes
how many clues must combine to use it.

### The seed (only explicit anchor)
- **C1 ★ (E–L)** Cindralok is a creature of **Fire**. *(explicit — required by design)*

### Element ↔ Ingredient links (the transitivity glue — one per element)
- **C2 ★ (L–I)** The reagent of **Fire** is the red-hot pepper → **Ghost Pepper**.
- **C3 ★ (L–I)** The reagent of **Water** is the vile fluid → **Vile Glomphidious**.
- **C4 ★ (L–I)** The reagent of **Earth** is the salt of stone → **Rock Salt**.
- **C5 ★ (L–I)** The reagent of the **Spirit** is the dream-flower → **Amaranth**.
- **C6 ★ (L–I)** The reagent of the **Body** is ground bone → **Bone Dust**.
  *(Air's reagent, Dogwheat, is left to fall out by elimination — see C12.)*

### Entity ↔ Element links (attach the remaining gods to elements, never to ingredients)
- **C7 ★ (E–L)** The **Fish God** rules the **Water**.
- **C8 ★ (E–L)** The **Iron God** holds the **Earth** (ore and stone are kin).
- **C9 ★ (E–L)** **Nytheris** is bound to the **Spirit** — she preys on the soul itself.
- **C10 ★ (E–L)** The **Bear** and the **stag** are the two beasts of blood; of the two,
  the **Bear** is the creature of the **Body** (flesh, sinew, the sleeping frame).
  *(Implies the stag is NOT Body; combined with C12 this pins the stag to Air.)*

### Negative / elimination confirmers
- **C11 ◇ (E–L)** The **stag** (Thistlebarrow) is no thing of flame, flood, stone, or
  soul. *(¬Fire ¬Water ¬Earth ¬Spirit for Thistlebarrow)*
- **C12 ★ (E–L, elimination)** Of all the powers, only the **stag** belongs to the open
  **Air**. *(pins Thistlebarrow = Air; the last element, so also confirms Bear = Body)*

> **Why no direct E–I clue:** every entity gets its ingredient only by first learning its
> **element** (E–L clue) and then applying the matching **L–I** clue. E.g.
> *C1 Cindralok=Fire + C2 Fire=Ghost Pepper ⇒ Cindralok=Ghost Pepper.* Two hops, always.

---

## 4. Transitive Solve Trace (proof it's forced & unique)

Elements first (from E–L clues):
- C1 → Cindralok = **Fire**
- C7 → Fish = **Water**
- C8 → Iron = **Earth**
- C9 → Nytheris = **Spirit**
- C10 → Bear = **Body** (and stag ≠ Body)
- Elements used: Fire, Water, Earth, Spirit, Body. Remaining element **Air** must go to the
  remaining entity **Thistlebarrow**. C12 confirms it directly; C11 corroborates. ✔
- **Entity↔Element fully forced.**

Ingredients via L–I glue (apply to each now-known element):
- Fire → C2 → Ghost Pepper ⇒ **Cindralok = Ghost Pepper**
- Water → C3 → Vile Glomphidious ⇒ **Fish = Vile Glomphidious**
- Earth → C4 → Rock Salt ⇒ **Iron = Rock Salt**
- Spirit → C5 → Amaranth ⇒ **Nytheris = Amaranth**
- Body → C6 → Bone Dust ⇒ **Bear = Bone Dust**
- Ingredients used: GP, VG, RS, Am, BD. Remaining ingredient **Dogwheat** must be **Air**'s,
  i.e. **Thistlebarrow = Dogwheat** (elimination). ✔
- **Element↔Ingredient and Entity↔Ingredient fully forced.**

Every fact is forced; nothing is used twice; the two leftovers (Air, Dogwheat) are unique.
**Solution is unique and solvable, and no single clue maps an entity straight to an
ingredient.** ∎

**Load-bearing set:** C1, C2–C6, C7–C10, C12 (11 clues). C11 is the lone pure-redundant
confirmer. Total raw clues: **12**.

---

## 5. Planned Lore Documents (8 docs, ~1–2 clues each)

Target: **8 documents** (up from last year's ~6). Spreading the 12 clues across 8 docs
means each doc carries only **1–2 clues** — no crammed 3-clue doc — which reads more
naturally and is easier to write/review. Each doc is a self-contained in-world lore piece
with an author/voice; the listed clues are the **bolded** facts hidden inside. Gating
conditions ("DO NOT OPEN unless…") to be tuned later in last-year style.


| Doc | Working Title | Voice / Type | Clues carried | Notes |
|-----|---------------|--------------|---------------|-------|
| **D1** | *A Bestiary of the Heart* (Cindralok entry) | Naturalist's catalogue entry | **C1** (Cindralok=Fire, explicit) + **C11** (the stag is none of flame/flood/stone/soul) | Opens the fire seed loudly; sneaks the stag negatives into a comparative aside. |
| **D2** | *A Cook's Cursed Recipe* | A village cook's recipe for a monstrous dish | **C2** (Fire→Ghost Pepper) + **C3** (Water→Vile Glomphidious) | The two reagents appear as recipe ingredients with their **elements named in the steps** ("a Ghost Pepper, a thing of pure Fire…"). Distinct artifact/voice — no longer a ledger. |
| **D3** | *A Judge's Ruling* | Court verdict quoting a merchant AND a bone-setter | **C4** (Earth→Rock Salt) + **C6** (Body→Bone Dust) | A fraud case: the merchant sold **sea salt** as Rock Salt and **chalk** as Bone Dust. The **bone-setter's rebuttal states the elemental truths** (Earth needs true Rock Salt; Body needs true Bone Dust) → delivers both pairings. Verdict: merchant fined for false advertising; bone-setter arrested for attempting to buy illegal bones. |
| **D4** | *The Alchemist's Journal — Eliminations* | Halbrecht Vunn, negative-inference notes | **C5** (Spirit→Amaranth, by elimination) | Vunn rules Amaranth OUT of the one rival element still open after D2+D3 (**¬Air**, core/load-bearing), plus a single margin **¬Body** confirmer, then names Spirit as the payoff. NOTE: reordered — D4 now carries **C5**, not C6 (C6 moved to D3). |
| **D5** | *Letter on the River-God* | Villager/pilgrim letter | **C7** (Fish=Water) | A traveler's account placing Uggglub to the Water. |
| **D6** | *The Forge-Warden's Testament* | Smith / miner's account | **C8** (Iron=Earth) | Ties Korrenvast to the deep stone/ore — Earth. |
| **D7** | *The Goat-Kin's Record of the Madness* | First-person, written **by a beastperson (goat)** — unsettling, not-quite-human logic | **C9** (Nytheris=Spirit) + **C10** (Bear=Body, stag≠Body, framed as a protective prayer) | A record of how **Nytheris drove the beastmen mad** (last year's plague) and how they were **cured when the Ancient Mask drove her influence from the land**. C9 emerges from her being the soul/Spirit-stealer who hollowed their minds. C10 is folded in as a **prayer of protection against Nytheris's return** — invoking the Bear as the god of the steadfast Body (flesh that cannot be hollowed), and noting the stag is a different sort of power. Voice: reverent but eerie; the goat counts in fives, trusts smells over words, fears still water/reflections. |
| **D8** | *The Stag's Own Verse* | Ballad / bard's song | **C12** (only the stag is of the Air) | The elimination capstone; a rousing dawn-song about horn on the wind. |

Clue coverage check: C1✔ C2✔ C3✔ C4✔ C5✔ C6✔ C7✔ C8✔ C9✔ C10✔ C11✔ C12✔ — all 12 placed.

### Premise / framing documents (P1–P2) — "Property of the Library"

Two additional player-facing documents establish the *shape* of the puzzle without giving
any pairing. Their covers read **"PROPERTY OF THE LIBRARY"** (not "DO NOT OPEN"), and they
carry **no bolded clue** — they only frame the two axes so players know what they are
solving. Files: `clue9.html`, `clue10.html`.

| Doc | Title | Establishes | Deliberately withheld |
|-----|-------|-------------|-----------------------|
| **P1** | *Of the Six Powers of the Deep Woods* | There are exactly **6 entities/powers** in the Deep Woods, each **bound to one of the 6 elements** (Fire/Water/Earth/Air/Spirit/Body), one-to-one. Names all six powers + all six elements. | **Which** power holds which element (no Entity↔Element pairing). No mention of ingredients. |
| **P2** | *Of the Six Reagents of the Art* | There are exactly **6 alchemical reagents**, each **answering to one of the 6 elements**, one-to-one. Names all six reagents + all six elements. | **Which** reagent answers to which element (no Ingredient↔Element pairing). No mention of the powers/entities. |

Design note: P1 + P2 hand players the two "columns" and the shared element spine, but never
connect entities↔ingredients (that link is forbidden as a stated clue anyway) and never
resolve any single element cell. They make the grid legible; the D1–D8 clues fill it in.


### Density note
- **8 documents.** D1, D2, D3, and D7 carry 2 clues each; D4, D5, D6, and D8 carry 1 clue
  each. No document carries 3. The three element→reagent documents are now **three
  distinct artifacts** (a cursed recipe, a judge's ruling, an alchemist's journal) rather
  than three near-identical ledger pages — this kills the "same page thrice" info-dump and
  reads far more naturally.

### Redundancy / safety
- Only C11 is fully redundant. If a group misses a document, they can often still finish:
  e.g. missing D8 (C12) is survivable because the Air/Dogwheat pair is the last leftover
  and falls out by elimination from the others. Missing an L–I document (D2/D3/D4) is
  the most punishing — consider making those the easiest to obtain.
- **D4 dependency note:** D4 delivers C5 (Spirit→Amaranth) by *elimination*, so it leans
  on D2+D3 being solved first (to know Fire/Water/Earth/Body reagents). To keep it solvable
  for weaker groups, Vunn still **names Spirit outright** as the payoff after the ¬Air
  reasoning — the eliminations are flavor + robustness, not the sole path.


---

## 6. Open Decisions Before Writing Clues

- **Difficulty confirm:** current design ≈ **2 hops per entity** (moderate). To push to
  hard, convert one E–L direct (e.g. C8 Iron=Earth) into a relational/negative chain.
- **Confirm inferred L–I mappings** still stand: Water=Vile Glomphidious, Air=Dogwheat
  (Fire/Ghost Pepper, Spirit/Amaranth, Body/Bone Dust, Earth/Rock Salt already set).
- **Which doc is "easiest to earn"** (recommend an L–I ledger page, since those are
  load-bearing).
- Then: write the actual lore prose into `clue.md` with the bolded clues + fold gates.

