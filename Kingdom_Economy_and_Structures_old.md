# Kingdom Economy & Structures System

## **1. Terrain & Worksites (Production)**

- Each hex of land can hold **one Worksite**.  
- The **terrain type** determines what it can produce:

| Terrain | Worksite Options | Yield/Turn |
| :---- | :---- | :---- |
| Plains | Farmstead | 2 Food |
| Forest | Logging Camp | 2 Lumber |
| Hills | Quarry **or** Farmstead | 1 Stone **or** 1 Food |
| Mountains | Mine **or** Quarry | 1 Ore **or** 1 Stone |
| Swamp | Hunting/Fishing Camp **or** Bog Mine | 1 Food **or** 1 Ore |
| Desert | — (unless Oasis special) | 0 (Oasis = 1 Food) |

- **Special hex traits** (e.g., Fertile, Rich Vein) add **+1 yield**.

---

## **2. Settlement Upkeep (Food Demand)**

- Settlements **consume Food** each turn:

| Settlement Size | Food Required/Turn |
| :---- | :---- |
| Village | 1 |
| Town | 4 |
| City | 8 |
| Metropolis | 12 |

- If unmet → **+1 Unrest per missing Food**.

## Military Support

Settlements provide the logistical foundation for supporting armies. Each settlement tier determines how many military units it can support. This represents the infrastructure, supply lines, and population base needed to field and maintain armies.

### Unit Capacity by Settlement Tier

| Settlement Tier | Unit Capacity |
|-----------------|---------------|
| Village (Tier 1) | 1 Unit |
| Town (Tier 2)    | 2 Units |
| City (Tier 3)    | 3 Units |
| Metropolis (Tier 4) | 4 Units |

### Rules for Military Support
- **Per Settlement:** Each settlement provides military support independently. Total unit capacity is the sum of all settlements in the kingdom.  
- **Unit Upkeep:** Units still require upkeep (Food and Gold), even if supported by a settlement. Military support determines only the maximum number of units that can be maintained without penalties.  
- **Exceeding Capacity:** If the kingdom fields more units than its total military support capacity, each excess unit increases **Unrest by 1 per Kingdom Turn**, reflecting the strain on the population and logistics.  
- **Structures and Modifiers:** Certain Structures (e.g., future military bases, barracks, fortresses) may enhance or modify unit support. Unless specified, the baseline unit capacity above applies.  
---
### Loss of Military Support

If a settlement is **lost, destroyed, or captured**, its unit capacity is immediately removed from the kingdom's total. If this causes the kingdom to exceed its military support capacity, the excess units are considered **unsupported**.

#### Unsupported Units
 
- At the start of each Kingdom Turn, each unsupported unit must attempt a **Morale check** to see if it holds together or disbands.

**Morale Check**
- **DC:** Use the Level-based DC for the unit's level.  
- **Skill:** The kingdom may roll **Diplomacy** (rallying loyalty) or **Intimidation** (enforcing discipline).  
- **Results:**  
  - **Critical Success:** The unit rallys for this turn, despite lack of supplies.
  - **Success:** The unit remains intact for this turn. **+1 Unrest**   
  - **Failure:** The unit disbands (soldiers desert or disperse). **+1 Unrest**  
  - **Critical Failure:** The unit disbands (soldiers defect,riot,or mutiny) **+2 Unrest** 

#### Ongoing Penalties
Each subsequent turn a unit remains unsupported, apply a **–1 penalty** to its Morale checks (–2 if the kingdom's Unrest is 10+). This reflects dwindling supplies, morale loss, and ongoing strain.  

---

### Example
A City (Tier 3) that supported 3 units is captured. The kingdom still fields those 3 units, but now they are **unsupported**.  
- Each unit must roll a Morale check at the start of the turn.  likly causing unrest
- If the war drags on, penalties accumulate and the risk of losing armies rises sharply.  

## **3. Storage**

- **Food is the primary stockpiled resource** (because it's consumed).  
- **LSO (Lumber, Stone, Ore)** must be used immediately or traded → otherwise lost.

### **Storage Progression**

- **Structures:** Expand storage capacity and resource types:

| Tier | Facility | Capacity |
| :---- | :---- | :---- |
| T1 Granary (Village+) | +4 Food |  |
| T2 Storehouses (Town+) | +8 Food, +4 Lumber |  |
| T3 Warehouses/Vaults (City+) | +16 Food, +8 Lumber, +4 Stone, +4 Ore |  |
| T4 Strategic Reserves (Metropolis) | +36 Food, +18 Lumber, +9 Stone, +9 Ore (immune to spoilage) |  |

---

## **4. Construction & Projects**

- **Buildings cost resources** (Lumber, Stone, Ore).  
- Costs scale by tier:  
  - Tier 1 (Village) → ~2 resources  
  - Tier 2 (Town) → ~4 resources  
  - Tier 3 (City) → ~8 resources  
  - Tier 4 (Metropolis) → ~16 resources

### **Build Queue**

- When a project starts, it has a **cost list** (e.g., 2 Lumber, 2 Stone, 4 Ore).  
- Each turn, **production from Works** is applied toward that cost.  
- When filled, the project is complete.  
- Excess production each turn:  
  - Can be **traded** (see Commerce).  
  - Otherwise **lost**.

---

## **5. Gold & Trade**

- Gold acts as a **wildcard resource**.  
- Conversion rates keep Gold weaker than direct resources:

| Conversion | Rate |
| :---- | :---- |
| Gold → Resource | 2 Gold = 1 Resource |
| Resource → Gold | 2 Resources = 1 Gold |

- **Commerce Structures** improve this efficiency:

| Facility | Effect |
| :---- | :---- |
| Market Square (Village+) | Enables baseline trade (2:1 both ways). |
| Trade Bazaar (Town+) | +1 Gold/turn income. |
| Merchant Guildhall (City+) | Improves sale rate → 3 Resources = 2 Gold. |
| Royal Bank (Metropolis) | Buy at 1:1 (sell stays weaker). |

---

## **6. Skill-Based Structures (Economic & Cultural Growth)**

- Each chain represents a **cultural/military/economic institution**.  
- Benefits scale:  
  - **T1:** Earn Income at Settlement lvl  
  - **T2:** Earn Income at Settlement lvl + 2 (+1 bonus)  
  - **T3:** Earn Income at Settlement lvl + 4 (+2 bonus)  
  - **T4:** Earn Income at Settlement lvl + 6 (+3 bonus) **+ Once per Kingdom Turn, reroll a failed skill check at this facility**

### **Example – Military & Training**

- T1: Sparring Ring → Athletics jobs at Settlement lvl.  
- T2: Training Yard → Athletics/Acrobatics jobs at Settlement lvl + 2, +1 bonus.  
- T3: Fighters' Guild → Athletics/Acrobatics/Intimidation jobs at Settlement lvl + 4, +2 bonus.  
- T4: Grand Coliseum → Same, but Settlement lvl + 6, +3 bonus, **reroll once/turn**.

*(All 9 skill chains follow this pattern with different skill mixes.)*

---

## **7. Summary Loop (Per Turn)**

1. **Production:** Works generate Food, Lumber, Stone, Ore.  
2. **Consumption:** Settlements eat Food; shortfall = Unrest.  
3. **Storage:** Food stored; LSO used immediately or traded.  
4. **Construction:** LSO fills build queues  
5. **Commerce:** Excess can be traded for Gold as a Kingdom Action  
   (2 resources:1 gold → better with banks).   
   Resources can be purchased as a Kingdom Action (1 gold: 2 resources)  
6. **Structures:** Generate Earn Income checks and bonuses.

---

## **8. Example Turn**

**Kingdom:** 1 Town (needs 4 Food).  
**Nearby hexes:**

- 2x Plains (Farmsteads = 4 Food)  
- 1x Forest (Logging Camp = 2 Lumber)  
- 1x Hills (Quarry = 1 Stone)

**Step 1 – Production:** 4 Food, 2 Lumber, 1 Stone.  
**Step 2 – Consumption:** Town eats 4 Food → stable (no unrest).  
**Step 3 – Storage:** Without Storehouses, no extra storage. Surplus = none.  
**Step 4 – Construction:** Building a Training Yard (needs 2 Lumber, 2 Stone).

- Apply 2 Lumber + 1 Stone this turn. 1 Stone remains owed.  
  **Step 5 – Commerce:** No surplus, nothing traded.  
  **Step 6 – Structures:** Town Hall provides Society jobs at Settlement lvl.

**Result:** Training Yard will complete next turn when 1 Stone is produced. Kingdom remains stable.

---

---
## Settlement Levels

Settlement tiers follow the official Pathfinder framework, with added structure prerequisites to reflect kingdom investment.

- **Village (Level 0–1)** – Entry-level settlement.  
- **Town (Level 2–4)** – Requires Village upgraded at Level 2+ and at least 2 Structures built. Unlocks Tier 2 structures.  
- **City (Level 5–7)** – Requires Town upgraded at Level 5+ and at least 4 Structures built. Unlocks Tier 3 structures.  
- **Metropolis (Level 8+)** – Requires City upgraded at Level 8+ and at least 6 Structures built. Unlocks Tier 4 structures and Great Works.  

These requirements ensure settlement growth is paced both by **level** and by **investment in structures**.
