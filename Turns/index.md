# Kingdom Turn Order

1. **Status Phase** - Gain Fame, apply ongoing modifiers
2. **Resource Phase** - Collect resources and revenue
3. **Unrest & Incidents Phase** - Calculate unrest, check for incidents
4. **Events Phase** - Check for kingdom events
5. **Action Phase** - Perform kingdom actions (4 PC actions)
6. **Upkeep Phase** - Food consumption, military support, build queue, end of turn

---
## Phase 1: Status 

### Gain Fame
* Gain **1 Fame** automatically at the start of each turn
* Fame can be spent to reroll any kingdom check (must take new result)
* Gain **1 Fame** when you critically succeed on a kingdom roll
* Fame does not carry over between turns (use it or lose it)

### Apply Permenant Modifiers
* some **Structures** reduce Unrest passively
* Other lingering modifiers from previous turns

---

## Phase 2: Resources

### Collect Resources and Revenue

**Resource Production by Terrain**

Each hex can hold one Worksite. Terrain determines production options:

| Terrain | Worksite Options | Yield/Turn |
|---------|-----------------|------------|
| Plains | Farmstead | 2 Food |
| Forest | Logging Camp | 2 Lumber |
| Hills | Quarry **or** Farmstead | 1 Stone **or** 1 Food |
| Mountains | Mine **or** Quarry | 1 Ore **or** 1 Stone |
| Swamp | Hunting/Fishing Camp **or** Bog Mine | 1 Food **or** 1 Ore |
| Desert | — (unless Oasis) | 0 (Oasis = 1 Food) |
| Water | 

**Special hex traits** (e.g., Fertile, Rich Vein) add **+1 yield**.

### Gold Income
* Settlements generate gold equal to their tier (if properly fed)
  * Village: 1 Gold | Town: 2 Gold | City: 3 Gold | Metropolis: 4 Gold
* Commerce structures may provide additional gold income
* Gold accumulates and carries over between turns

---

## Phase 3: Unrest

### Calculate Unrest

**Passive Unrest Sources:**
* **If at War:** +1 Unrest per turn
* **Territory Size:**
  * 8-15 hexes: +1 Unrest per turn
  * 16-23 hexes: +2 Unrest per turn
  * 24-31 hexes: +3 Unrest per turn
  * 32+ hexes: +4 Unrest per turn
* **Each Metropolis:** +1 Unrest per turn
* **Hostile Nations:** +1 Unrest per hostile nation per turn

**Unrest Tiers and Penalties:**
* **Tier 0: Stable (0-2)** - No penalty, no incidents
* **Tier 1: Discontent (3-5)** - -1 penalty to all checks
* **Tier 2: Turmoil (6-8)** - -2 penalty to all checks
* **Tier 3: Rebellion (9+)** - -3 penalty to all checks (capped)

### Check for Incidents

If Unrest is Tier 1 or higher, immediately roll d100 on the appropriate incident table (see Unrest_incidents.md):
* **Tier 1:** Minor Incidents (80% chance an incident occurs)
* **Tier 2:** Moderate Incidents (85% chance an incident occurs)
* **Tier 3:** Major Incidents (90% chance an incident occurs)

**Important:** Resolving incidents requires a skill check but does NOT consume a Kingdom Action.

---

## Phase 4: Events

### Check for Kingdom Events

* Roll a **flat check DC 16**
* **Success:** A random **Kingdom Event** occurs this turn (see Events.md)
* **Failure:** No event; **DC reduces by 5** for next turn (minimum DC 6)
* **After an event occurs,** the DC **resets to 16**

Players can spend an action to resolve a kingdom event, or aid another in doing so.

---

## Phase 5: Action Phase

### Perform Kingdom Actions

This is the main decision-making phase where players shape the kingdom.

**Action Rules:**
* Each of the **4 PCs** takes **one** Kingdom Action per turn (4 total actions)
* Actions taken from the **Capital** gain a **+1 circumstance bonus**
* All players declare their actions, then resolve them
* All checks use **Level-Based DCs** based on Party Level
* Critical successes grant +1 Fame
* Only certain critical failures cause +1 Unrest (crisis/military actions)

**Action Categories:**

#### Uphold Stability
- Arrest Dissidents
- Execute or Pardon Prisoners
- Deal with Unrest

#### Military Operations
- Recruit a Unit
- Outfit Army
- Deploy Army
- Recover Army
- Train Army
- Disband Army

#### Expand the Borders
- Claim Hexes
- Build Roads
- Send Scouts
- Fortify Hex
- Create Worksite

#### Urban Planning
- Establish a Settlement
- Upgrade a Settlement
- Build Structure
- Repair Structure

#### Foreign Affairs
- Establish Diplomatic Relations
- Request Economic Aid
- Request Military Aid
- Infiltration
- Hire Adventurers

#### Economic Actions
- Sell Surplus
- Purchase Resources
- Harvest Resources
- Collect Stipend

*For complete action details, see Actions.md*

---

## Phase 6: Upkeep Phase

### Food Consumption

Settlements consume food based on tier:
* **Village:** 1 Food
* **Town:** 4 Food
* **City:** 8 Food
* **Metropolis:** 12 Food

**Food Allocation Priority:** Settlements are fed in tier order (highest to lowest)

**Food Shortages:** Unfed settlements generate Unrest equal to their tier
* Village: +1 Unrest | Town: +2 Unrest | City: +3 Unrest | Metropolis: +4 Unrest

**Armies:** Each army requires 1 Food per turn (causes +1 Unrest if unfed)

**Storage Structures:**
* T1 Granary: +4 Food capacity
* T2 Storehouses: +8 Food, +4 Lumber
* T3 Warehouses: +16 Food, +8 Lumber, +4 Stone, +4 Ore
* T4 Strategic Reserves: +36 Food, +18 Lumber, +9 Stone, +9 Ore (immune to spoilage)

### Military Support

**Army Capacity:** Sum of all settlements' support values
* Village: 1 Army | Town: 2 Armies | City: 3 Armies | Metropolis: 4 Armies

**Unsupported Armies:** Each excess army makes a Morale check (Diplomacy or Intimidation vs Level-based DC)
* **Critical Success:** Army rallies despite lack of supplies
* **Success:** Army remains, **+1 Unrest**
* **Failure:** Army disbands, **+1 Unrest**
* **Critical Failure:** Army disbands (mutiny/defection), **+2 Unrest**

**Penalties:** Each turn unsupported: –1 to Morale checks (–2 if Unrest 10+)

### Build Queue

**Resource Application:**
* Production automatically applies to current construction project each turn
* Projects complete when all resource costs are met
* Unused Lumber, Stone, and Ore are **lost at end of turn**

**Resource Requirements by Tier:**
* Tier 1: ~2 resources total
* Tier 2: ~4 resources total
* Tier 3: ~8 resources total
* Tier 4: ~16 resources total

**Trade Rates:**
* **Base:** 2 Resources → 1 Gold | 2 Gold → 1 Resource
* Commerce structures improve these rates (see Structures.md)

### End of Turn Resolution

* **Unresolved Events:** Apply Failure result for any events not addressed
  * Events become Continuous and persist into next turn
  * See Events.md for details
* Process all consequences from the turn
* Carry over stored resources (Gold and Food in storage structures)
* Clear single-turn effects and prepare for next turn

---

## Example Turn

See Turn_Example.md for a complete walkthrough of a kingdom turn in action.
