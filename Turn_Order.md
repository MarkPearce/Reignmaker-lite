# **Cohesive Kingdom Gameplay Loop**

## **1\. Gain Fame**

Fame represents your kingdom's reputation and standing in the world. It can help you overcome challenges during critical moments.

* Gain **1 Fame** automatically at the start of each turn
* A Fame point may be spent to reroll a **kingdom roll** (must take new result)
* Whenever you **critically succeed** on a kingdom roll, gain **1 Fame**
* Fame does not carry over between turns unless specifically noted
* There is no maximum Fame limit during a turn

## **2\. Apply Ongoing Modifiers & Check for Incidents**

At the start of each turn, account for persistent effects and resolve any unrest incidents.

### Passive Unrest Sources
* **If at War:** +1 Unrest per turn
* **Territory Size:**
  - 8-15 hexes: +1 Unrest per turn
  - 16-23 hexes: +2 Unrest per turn
  - 24-31 hexes: +3 Unrest per turn
  - 32+ hexes: +4 Unrest per turn
* **Each Metropolis:** +1 Unrest per turn

### Unrest Tiers and Penalties
* **Tier 0: Stable (0-2)** - No penalty, no incidents
* **Tier 1: Discontent (3-5)** - -1 penalty to all checks
* **Tier 2: Turmoil (6-8)** - -2 penalty to all checks
* **Tier 3: Rebellion (9+)** - -3 penalty to all checks (capped)

### Incident Check
If Unrest is Tier 1 or higher, immediately roll d100 on the appropriate incident table:
* **Tier 1:** Minor Incidents (20% chance of no incident)
* **Tier 2:** Moderate Incidents (15% chance of no incident)
* **Tier 3:** Major Incidents (10% chance of no incident)

**Important:** Resolving incidents requires a skill check but does NOT consume a Kingdom Action. These are immediate crises that interrupt normal business.

### Other Modifiers
* Certain **Structures** reduce Unrest passively (Theater -1/turn, etc.)
* Events may apply ongoing effects from previous turns

## **3\. Check for Kingdom Events**

Random events will challenge your Kingdom. The longer you go without an event, the more likely one becomes..

* At the start of the turn, roll a **flat check DC 16**  
* **Success:** A random **Kingdom Event** occurs this turn  
* **Failure:** No event; next turn the **DC is reduced by 5**  
* **After an event occurs,** the DC **resets to 16**  
* Players may later use Actions to **resolve or mitigate** events

## **4\. Manage Resources**

Your kingdom's resources must be carefully balanced each turn. This phase covers food production, military support, construction materials, and revenue generation.

**Resource Types:**
* **Food** - Required for population and army upkeep, can be stored
* **Lumber** - Used for buildings and roads (must be used or traded each turn)
* **Stone** - Used for fortifications and structures (must be used or traded each turn)
* **Ore** - Used for weapons and advanced buildings (must be used or traded each turn)
* **Gold** - Flexible resource for trade, upkeep, and special actions (accumulates)

### **Resource Production by Terrain**

Each hex can hold one Worksite. Terrain determines production options:

| Terrain | Worksite Options | Yield/Turn |
|---------|-----------------|------------|
| Plains | Farmstead | 2 Food |
| Forest | Logging Camp | 2 Lumber |
| Hills | Quarry **or** Farmstead | 1 Stone **or** 1 Food |
| Mountains | Mine **or** Quarry | 1 Ore **or** 1 Stone |
| Swamp | Hunting/Fishing Camp **or** Bog Mine | 1 Food **or** 1 Ore |
| Desert | — (unless Oasis) | 0 (Oasis = 1 Food) |

Special hex traits (e.g., Fertile, Rich Vein) add **+1 yield**.

### **Food Management**

Food is essential for keeping your population fed and content. Shortfalls lead to unrest, while surpluses can be stored for future needs.

* **Consumption:** Each Settlement consumes Food (Village 1, Town 4, City 8, Metropolis 12)  
* **Shortfall:** Food shortage causes Unrest gain at 1:1 ratio  
* **Storage Structures:**
  * T1 Granary (Village+): +4 Food capacity
  * T2 Storehouses (Town+): +8 Food, +4 Lumber capacity
  * T3 Warehouses (City+): +16 Food, +8 Lumber, +4 Stone, +4 Ore capacity
  * T4 Strategic Reserves (Metropolis): +36 Food, +18 Lumber, +9 Stone, +9 Ore (immune to spoilage)

### **Military Support**

Armies require proper support infrastructure to maintain morale and effectiveness. Exceeding your support capacity creates problems.

* **Unit Limits:** The sum of all settlements' tier levels determines total supported units (Village 1, Town 2, City 3, Metropolis 4, modified by structures)  
* **Unsupported Units:** Must make Morale checks (Diplomacy or Intimidation vs Level-based DC)
  * Critical Success: Unit rallies despite lack of supplies
  * Success: Unit remains, +1 Unrest
  * Failure: Unit disbands, +1 Unrest
  * Critical Failure: Unit disbands (mutiny/defection), +2 Unrest
* **Penalties:** Each turn unsupported: –1 to Morale checks (–2 if Unrest 10+)

### **Construction Resources & Build Queue**

Lumber, Stone, and Ore are vital for building projects. These resources must be used immediately or they are lost, representing the perishable nature of prepared materials.

* **Collection:** Each hex with a Worksite generates resources (see terrain table above)  
* **Build Queue:** Projects have cost requirements that can be filled over multiple turns
  * Tier 1 structures: ~2 resources total
  * Tier 2 structures: ~4 resources total
  * Tier 3 structures: ~8 resources total
  * Tier 4 structures: ~16 resources total
* **Application:** Production automatically applies to current project each turn
* **Completion:** Project finishes when all resource costs are met
* **Loss:** Any Lumber, Stone, or Ore not used or traded by the end of the turn is lost

### **Revenue Generation & Commerce**

Gold represents your kingdom's liquid wealth and economic power. Unlike construction resources, gold accumulates over time and provides flexibility.

* **Gold Income:** Generated by structures (Markets, Counting Houses, etc.)  
* **Accumulation:** Gold carries over between turns  
* **Usage:** Spent on upkeep, hiring, events, or trade
* **Trade Rates:** Default 2:1 both ways (2 resources = 1 gold, 2 gold = 1 resource)
  * Commerce structures improve these rates:
  * T2 Trade Bazaar: +1 Gold/turn income
  * T3 Merchant Guildhall: Improves sale to 3 resources = 2 gold
  * T4 Royal Bank: Buy at 1:1 (gold to resources)

## **5\. Perform Kingdom Actions**

This is the active decision-making phase where the four player characters shape the kingdom's development through strategic actions.

### **Action Rules:**
* Each of the **4 PCs** takes **one** Kingdom Action per turn (4 total actions)
* Actions taken from the **Capital** gain a **+1 Circumstance Bonus**
* Actions marked with **#** may only be taken **once per Kingdom Turn**
* **Before** resolving actions, all players declare their actions, then skill checks are rolled
* All checks use **Level-Based DCs** based on Party Level (see level_DC_progression.md)
* Critical successes grant +1 Fame
* Only certain critical failures cause +1 Unrest (military/crisis actions)

### **Available Actions:**

**Uphold Stability:** Maintain the kingdom's cohesion by resolving crises and quelling unrest
* *Provide Support:* Aid another PC's Kingdom Action
* *Resolve a Kingdom Event:* Rise to meet disasters, uprisings, or opportunities
* *Execute or Pardon Prisoners:* Deal with imprisoned unrest through justice
* *Deal with Unrest:* Directly reduce unrest by 1-3 based on success
* *Arrest Dissidents:* Convert current unrest to imprisoned unrest

**Military Operations:** War must be waged with steel and strategy
* *Recruit a Unit:* Raise new troops for your armies
* *Outfit Army:* Equip troops with armor, weapons, runes, or equipment
* *Deploy Army:* Move troops to strategic positions
* *Recover Army:* Heal and restore damaged units
* *Train Army:* Improve unit levels up to party level
* *Disband Army:* Decommission troops and return soldiers home

**Expand the Borders:** Seize new territory to grow your influence and resources
* *Claim Hexes:* Add new territory to your kingdom
* *Build Roads:* Connect your territory with infrastructure
* *Send Scouts:* Learn about unexplored hexes
* *Fortify Hex:* Strengthen defensive positions
* *Create Worksite:* Establish farms, mines, quarries, or lumber camps

**Urban Planning:** Your people need places to live, work, trade, and worship
* *Establish a Settlement:* Found a new village
* *Upgrade a Settlement:* Advance tiers (requires both level and structure prerequisites)
  * Village → Town: Level 2+ and 2+ structures
  * Town → City: Level 5+ and 4+ structures  
  * City → Metropolis: Level 8+ and 8+ structures
* *Develop a Settlement:* Add markets, temples, barracks, and other structures

**Foreign Affairs:** No kingdom stands alone
* *Establish Diplomatic Relations:* Form alliances with other nations
* *Request Economic Aid:* Ask allies for resources or gold
* *Request Military Aid:* Call for allied troops in battle
* *Infiltration:* Gather intelligence through espionage
* *Hire Adventurers:* Pay gold to resolve events (2 Gold cost)

**Economic Actions:** Manage trade and personal wealth
* *Sell Surplus:* Trade 2 resources for gold
* *Purchase Resources:* Spend 2 gold for resources
* *Collect Resources:* Gather from hexes with or without worksites
* *Collect Stipend:* Extract personal income (requires Counting House)

*Note: Trading and stipends are not automatic; they require Actions during this phase.*

## **6\. End of Turn Resolution**

The final phase wraps up the current turn and prepares for the next. All lingering effects are processed and the kingdom's status is updated.

* Apply lingering effects from unresolved Events  
* Process consequences of unsupported armies (if not already handled)  
* Carry over stored resources (Gold and any stored Food in storage structures)  
* Clear any single-turn effects and prepare for next turn
