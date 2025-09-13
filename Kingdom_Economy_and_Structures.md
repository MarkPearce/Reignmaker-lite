# Kingdom Economy & Structures Reference

This document provides supplementary details for kingdom management structures and economic systems.

---

## Settlement Levels & Structure Limits

Settlement advancement is gated by both **level thresholds** and **structure prerequisites**:

| Tier       | Level Range | Max Structures | Advancement Requirement |
|------------|-------------|----------------|-----------------------------
| Village    | 0–1         | 2              | Level 2 + 2 structures → Town |
| Town       | 2–4         | 4              | Level 5 + 4 structures → City |
| City       | 5–7         | 8              | Level 8 + 8 structures → Metropolis |
| Metropolis | 8+          | Unlimited      | — |

Each tier unlocks access to more advanced structures:
- **Village (Tier 1):** Basic structures only
- **Town (Tier 2):** Unlocks Tier 2 structures
- **City (Tier 3):** Unlocks Tier 3 structures
- **Metropolis (Tier 4):** Unlocks Tier 4 structures and Great Works

---

## Skill-Based Structures (Economic & Cultural Growth)

Each chain represents a **cultural/military/economic institution** that provides Earn Income opportunities.

### Benefit Scaling
- **T1:** Earn Income at Settlement level
- **T2:** Earn Income at Settlement level + 2 (+1 bonus)
- **T3:** Earn Income at Settlement level + 4 (+2 bonus)
- **T4:** Earn Income at Settlement level + 6 (+3 bonus) **+ Once per Kingdom Turn, reroll a failed skill check at this facility**

### Example Chain – Military & Training
- **T1 Sparring Ring:** Athletics jobs at Settlement level
- **T2 Training Yard:** Athletics/Acrobatics jobs at Settlement level + 2, +1 bonus
- **T3 Fighters' Guild:** Athletics/Acrobatics/Intimidation jobs at Settlement level + 4, +2 bonus
- **T4 Grand Coliseum:** Same skills, Settlement level + 6, +3 bonus, **reroll once/turn**

*(All 9 skill chains follow this pattern with different skill mixes)*

---

## Example Kingdom Turn

**Kingdom:** 1 Town (needs 4 Food)  
**Controlled hexes:**
- 2x Plains with Farmsteads = 4 Food
- 1x Forest with Logging Camp = 2 Lumber
- 1x Hills with Quarry = 1 Stone

### Turn Sequence:

**Phase 1 – Gain Fame:** Start with 1 Fame (can spend to reroll kingdom checks)

**Phase 2 – Apply Modifiers:** Check for war status, structure bonuses, etc.

**Phase 3 – Kingdom Event:** Roll DC 16 flat check (no event this turn)

**Phase 4 – Manage Resources:**
- **Production:** 4 Food, 2 Lumber, 1 Stone
- **Consumption:** Town consumes 4 Food → balanced (no unrest)
- **Storage:** Without Storehouses, no extra storage capacity
- **Construction:** Building a Training Yard (costs 2 Lumber, 2 Stone total)
  - Apply 2 Lumber + 1 Stone this turn
  - 1 Stone still needed to complete

**Phase 5 – Kingdom Actions:** Leaders take their actions

**Phase 6 – End of Turn:** 
- No surplus resources to carry over (LSO not used is lost)
- Training Yard will complete next turn when final Stone is produced

**Result:** Kingdom remains stable, construction progressing.

---

## Commerce Structure Effects

Commerce structures improve trade efficiency:

| Structure | Tier | Effect |
|-----------|------|--------|
| Market Square | T1 (Village+) | Enables baseline trade (2:1 both ways) |
| Trade Bazaar | T2 (Town+) | +1 Gold/turn income |
| Merchant Guildhall | T3 (City+) | Improves sale rate to 3 Resources = 2 Gold |
| Royal Bank | T4 (Metropolis) | Buy resources at 1:1 (gold to resources) |

---

*For complete gameplay rules and turn sequence, see gameplay_loop.md*  
*For specific Kingdom Actions, see Kingdom_Actions.md*
