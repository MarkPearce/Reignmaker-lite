# Resources

Resource production forms the economic backbone of your kingdom. Each hex of controlled territory generates resources based on its terrain type and the worksite you construct there. Food sustains your settlements and armies, while Lumber, Stone, and Ore provide the raw materials needed for construction and development. Strategic placement of worksites based on terrain advantages and kingdom needs is crucial for maintaining a thriving realm.

## Resource Collection

**Resource Types:**<br>
- **Food** - Required for population and army upkeep, can be stored
- **Lumber** - Used for buildings and roads (must be used or traded each turn)
- **Stone** - Used for fortifications and structures (must be used or traded each turn)
- **Ore** - Used for weapons and advanced buildings (must be used or traded each turn)
- **Gold** - Flexible resource for trade, upkeep, and special actions (accumulates)

## Terrain and Worksites

Each hex of land can hold **one Worksite**. The **terrain** determines what it can produce:

| Terrain | Worksite Options | Yield/Turn |
| :---- | :---- | :---- |
| Plains | Farmstead | 2 Food |
| Forest | Logging Camp | 2 Lumber |
| Hills | Quarry **or** Farmstead | 1 Stone **or** 1 Food |
| Mountains | Mine **or** Quarry | 1 Ore **or** 1 Stone |
| Swamp | Hunting/Fishing Camp **or** Bog Mine | 1 Food **or** 1 Ore |
| Desert | — (unless Oasis special) | 0 (Oasis = 1 Food) |
| Water | 1 Food (no worksite needed) | counts as road

**Special hex traits** (e.g., Fertile, Rich Vein) add **+1 yield** to production.

## Food Consumption

Settlements require food to sustain their populations. Food shortages directly create unrest.

**Consumption by Settlement Tier:**
| Settlement | Food Required/Turn |
|------------|-------------------|
| Village | 1 Food |
| Town | 4 Food |
| City | 8 Food |
| Metropolis | 12 Food |

**Food Shortage Consequences:**
- **Unfed Settlement:** Any settlement that receives less than its full food requirement generates Unrest equal to its settlement tier
- Village: +1 Unrest | Town: +2 Unrest | City: +3 Unrest | Metropolis: +4 Unrest
- Example: A City needs 8 Food but only receives 5 → +3 Unrest (tier 3)

**Food Allocation Priority:**
- Settlements are fed in tier order from highest to lowest (Metropolis → City → Town → Village)
- Each settlement receives its full food requirement before the next tier is fed
- This automatic allocation ensures higher-tier settlements are prioritized
- If insufficient food remains for a settlement, it receives no food and generates tier-based Unrest

"let them eat cake"

**Food Storage:**
- Food is the **only resource that can be stored** between turns
- Storage capacity depends on structures:
  - **T1 Granary:** +4 Food capacity
  - **T2 Storehouses:** +8 Food, +4 Lumber capacity
  - **T3 Warehouses:** +16 Food, +8 Lumber, +4 Stone, +4 Ore capacity
  - **T4 Strategic Reserves:** +36 Food, +18 Lumber, +9 Stone, +9 Ore (immune to spoilage)

## Military Support Costs

Armies require infrastructure and supply lines. Exceeding your support capacity strains the kingdom.

**Army Food Consumption:**
- Each army requires **1 Food per turn** regardless of support status
- This food requirement is in addition to settlement consumption
- Food shortages for armies count toward unrest just like settlement shortages

**Army Support Capacity:**
| Settlement | Armies Supported |
|------------|-------------------|
| Village | 1 Army |
| Town | 2 Armies |
| City | 3 Armies |
| Metropolis | 4 Armies |

**Total Capacity:** Sum of all settlements' support values

**Unsupported Armies:**
When you have more armies than your capacity supports:
- Each unsupported army must make a **Morale check** (Diplomacy or Intimidation vs Level-based DC)
  - **Critical Success:** Army rallies despite lack of supplies
  - **Success:** Army remains, **+1 Unrest**
  - **Failure:** Army disbands, **+1 Unrest**
  - **Critical Failure:** Army disbands (mutiny/defection), **+2 Unrest**
- **Ongoing Penalty:** -1 to Morale checks for each turn an army remains unsupported (-2 if Unrest 10+)

## Build Queue Management

Construction resources (Lumber, Stone, Ore) must be used immediately or they are lost.

**Resource Application:**
- Production automatically applies to current construction project each turn
- Structures have tiered resource costs:
  - **Tier 1:** ~2 resources total
  - **Tier 2:** ~4 resources total
  - **Tier 3:** ~8 resources total
  - **Tier 4:** ~16 resources total
- Project completes when all resource costs are met
- **Important:** Lumber, Stone, and Ore not used for construction or traded are **lost at end of turn**

## Trade and Commerce

Trading requires a Kingdom Action during Phase 5 - it is not automatic. Resources can be converted to/from gold, though at unfavorable base rates:

**Base Trade Rates:**

- **Sell Resources:** 2 Resources → 1 Gold
- **Purchase Resources:** 2 Gold → 1 Resource

**Commerce Structure Improvements:**
- **T2 Trade Bazaar:** +1 Gold/turn income
- **T3 Merchant Guildhall:** Sell at 3 Resources → 2 Gold
- **T4 Royal Bank:** Buy at 1:1 (Gold to Resources)

## Construction Queue

Structures require resources to build, with costs scaling by tier. When a construction project begins, resources produced each turn are automatically applied toward the project's cost. Once all required resources are provided, the structure is complete.

**Resource Requirements by Tier:**
- **Tier 1 (Village):** ~2-4 total resources
- **Tier 2 (Town):** ~4-6 total resources  
- **Tier 3 (City):** ~8-10 total resources
- **Tier 4 (Metropolis):** ~14-18 total resources

Each turn, your worksites' production automatically fills the construction queue. Resources not used for construction can be traded for gold through Commerce structures, or are lost at the end of the turn.

## Gold & Trade

Gold serves as a flexible currency that can be converted to and from resources, though at unfavorable base rates to encourage direct resource production.

**Base Conversion Rates:**
- **Purchase Resources:** 2 Gold → 1 Resource
- **Sell Resources:** 2 Resources → 1 Gold

Commerce structures improve these conversion rates and provide additional benefits (see Structures.md for Commerce category under Support Structures). Resources that are neither used for construction nor traded are lost at the end of each Kingdom Turn.

## Insufficient Resources (Events & Incidents)

When an event or incident requires payment of resources (gold, food, lumber, stone, or ore) and you cannot afford the full cost:

- **Lose what you have:** Reduce the resource to 0
- **Gain +1 Unrest:** A flat penalty for any resource shortage (not per resource)
- **Message:** "You gained 1 unrest from shortage."

**Important:** This rule applies ONLY to events and incidents. Settlement food consumption and army support costs use their own tier-based Unrest calculations (see Food Consumption and Military Support Costs sections above).

**Example:** An incident requires you to lose 5 gold, but you only have 3 gold. You lose 3 gold (reduced to 0) and gain +1 Unrest from shortage.
