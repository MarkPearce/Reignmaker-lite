# Kingdom Rules

This document provides  details for kingdom management structures and economic systems.

---

## **Resource Production**

Resource production forms the economic backbone of your kingdom. Each hex of controlled territory generates resources based on its terrain type and the worksite you construct there. Food sustains your settlements and armies, while Lumber, Stone, and Ore provide the raw materials needed for construction and development. Strategic placement of worksites based on terrain advantages and kingdom needs is crucial for maintaining a thriving realm.

### **Terrain and Worksites** 

- Each hex of land can hold **one Worksite**.  
- The **terrain** determines what it can produce:

| Terrain | Worksite Options | Yield/Turn |
| :---- | :---- | :---- |
| Plains | Farmstead | 2 Food |
| Forest | Logging Camp | 2 Lumber |
| Hills | Quarry **or** Farmstead | 1 Stone **or** 1 Food |
| Mountains | Mine **or** Quarry | 1 Ore **or** 1 Stone |
| Swamp | Hunting/Fishing Camp **or** Bog Mine | 1 Food **or** 1 Ore |
| Desert | — (unless Oasis special) | 0 (Oasis = 1 Food) |

- **Special hex traits** (e.g., Fertile, Rich Vein) may increase yield or provide additional benefits.

### **Storage**

- **Food is the only stockpiled resource**
- **Resources (Lumber, Stone, Ore)** must be used or traded on the turn they are acquired otherwise, they are lost at the end of the turn.
- Excess Resources can be traded for Gold as a Kingdom Action (2 resources: gold. The ratio improves with structures). 
- Resources can be purchased as a Kingdom Action (1 gold: 2 resources)


## Settlements

Settlements are the heart of your kingdom, representing population centers that drive growth, cultural development, and military power. From humble villages to sprawling metropolises, each settlement serves as a hub for resource consumption, structure construction, and army support. As settlements grow in size and sophistication, they unlock access to more advanced structures, support larger military forces, and become centers of specialized knowledge and industry. The careful development and protection of settlements forms the cornerstone of any successful kingdom's strategy.

### Settlement Levels & Structure Limits

Settlement advancement is gated by both **level thresholds** and **structure prerequisites**.
To advance to the next tier of settlement, you must:
1. First reach the **maximum number of structures** for your current tier
2. Then promote your settlement level to the minimum threshold of the next tier

| Settlement | Tier       | Food/Turn | Level Range | Max Structures | Advancement Requirement |
|------------|-------------|----------------|-----------------------------|-----------------------------|-----------------------------|
| Village | 1    | 1   | 0–1         | 2              | Level 2 + 2 structures → Town |
| Town   | 2       | 4      | 2–4         | 4              | Level 5 + 4 structures → City |
| City   | 3      | 8     | 5–7         | 8              | Level 8 + 8 structures → Metropolis |
| Metropolis | 4 | 12 | 8+          | Unlimited      | — |

**A settlement without the maximum number of structures may not exceed its current tier's level range.** For example, a Town with only 3 structures cannot advance beyond level 4, until it has all 4 structures built.

Each tier unlocks access to more advanced structures:
- **Village (Tier 1):** Basic structures only
- **Town (Tier 2):** Unlocks Tier 2 structures
- **City (Tier 3):** Unlocks Tier 3 structures
- **Metropolis (Tier 4):** Unlocks Tier 4 structures and Great Works

---

## Structures

Structures are buildings that define your settlements' capabilities and character. From humble markets to coliseums and fortresses, each structure provides unique benefits that enhance your kingdom's economy, culture, or military. Structures are tiered according to settlement size—villages can only support basic structures (T1), while metropolises can construct the most advanced buildings (T4). Structures shape your kingdom's capabilities, focusing on trade, military training, cultural development, or resource management.

### Skill-Based Structures (Economic & Cultural Growth)

Skill structures are specialized buildings where citizens work and train, allowing them to use earn income. Each structure chain progresses from basic facilities to grand institutions. 

#### Benefit Scaling
- **T1:** Earn Income at up to Settlement level
- **T2:** Earn Income at up to Settlement level + 2 (+1 circumstance bonus to skill checks)
- **T3:** Earn Income at up to Settlement level + 4 (+2 bonus bonus to skill checks)
- **T4:** Earn Income at up to Settlement level + 6 (+3 bonus bonus to skill checks)
    **Once per Kingdom Turn, reroll a failed skill check at this facility**

#### Skill Categories and Associated Skills

- **Crime & Intrigue** (Thievery, Deception, Stealth)
- **Civic & Governance** (Society, Diplomacy, Deception)
- **Military & Training** (Athletics, Acrobatics, Intimidation)
- **Crafting & Trade** (Crafting, Lore, Society)
- **Knowledge & Magic** (Lore, Arcana, Occultism)
- **Faith & Nature** (Religion, Medicine, Nature)
- **Medicine & Healing** (Medicine, Lore, Arcana)
- **Performance & Culture** (Performance, Diplomacy, Lore)
- **Exploration & Wilderness** (Survival, Nature, Stealth)

### Support Structures (Economic & Cultural Growth)

Support structures provide essential infrastructure for kingdom management, from storage and defense to commerce and cultural institutions. Unlike skill-based structures that focus on earning income through specialized labor, support structures offer passive benefits and strategic advantages that strengthen your kingdom's foundation.

#### Support Structure Categories

- **Food Storage** - Preserve agricultural surplus
- **Fortifications** - Defensive walls and battlements
- **Logistics** - Military housing and support
- **Commerce** - Trade and resource conversion
- **Culture** - Morale and unrest management
- **Revenue** - Tax collection and treasury

---

## Construction & Trade

### Construction Queue

Structures require resources to build, with costs scaling by tier. When a construction project begins, resources produced each turn are automatically applied toward the project's cost. Once all required resources are provided, the structure is complete.

**Resource Requirements by Tier:**
- **Tier 1 (Village):** ~2-4 total resources
- **Tier 2 (Town):** ~4-6 total resources  
- **Tier 3 (City):** ~8-10 total resources
- **Tier 4 (Metropolis):** ~14-18 total resources

Each turn, your worksites' production automatically fills the construction queue. Resources not used for construction can be traded for gold through Commerce structures, or are lost at the end of the turn.

### Gold & Trade

Gold serves as a flexible currency that can be converted to and from resources, though at unfavorable base rates to encourage direct resource production.

**Base Conversion Rates:**
- **Purchase Resources:** 2 Gold → 1 Resource
- **Sell Resources:** 2 Resources → 1 Gold

Commerce structures improve these conversion rates and provide additional benefits (see Commerce category under Support Structures). Resources that are neither used for construction nor traded are lost at the end of each Kingdom Turn.

---

## Military Management

Settlements provide the logistical foundation for supporting armies. This represents the infrastructure, supply lines, and population base needed to field and maintain armies. The military capacity of your kingdom determines how many armies you can sustain without straining your population and resources.

### Army Capacity by Settlement Tier

Each settlement provides military support based on its tier. The kingdom's total army capacity is the sum of all settlements' individual capacities.

| Settlement Tier | Army Capacity |
|-----------------|---------------|
| Village (Tier 1) | 1 Army |
| Town (Tier 2)    | 2 Armies |
| City (Tier 3)    | 3 Armies |
| Metropolis (Tier 4) | 4 Armies |

**Exceeding Capacity:** If the kingdom fields more armies than its total military support capacity, each excess army increases **Unrest by 1 per Kingdom Turn**, reflecting the strain on the population and logistics.

**Structures and Modifiers:** Certain Structures (e.g., Barracks, Garrison, Fortress, Citadel) may enhance army support capacity. Unless specified, the baseline army capacity above applies.

### Loss of Military Support

If a settlement is **lost, destroyed, or captured**, its army capacity is immediately removed from the kingdom's total. If this causes the kingdom to exceed its military support capacity, the excess armies are considered **unsupported**.

#### Unsupported Armies

At the start of each Kingdom Turn, each unsupported army must attempt a **Morale check** to see if it holds together or disbands.

**Morale Check**
- **DC:** Use the Level-based DC for the army's level  
- **Skill:** The kingdom may roll **Diplomacy** (rallying loyalty) or **Intimidation** (enforcing discipline)

| Result | Effect |
|--------|--------|
| **Critical Success** | The army rallies for this turn, despite lack of supplies |
| **Success** | The army remains intact for this turn. **+1 Unrest** |
| **Failure** | The army disbands (soldiers desert or disperse). **+1 Unrest** |
| **Critical Failure** | The army disbands (soldiers defect, riot, or mutiny). **+2 Unrest** |

**Ongoing Penalties**  
Each subsequent turn an army remains unsupported, apply a **–1 circumstance penalty** to its Morale checks. This reflects dwindling supplies, morale loss, and ongoing strain.

#### Example
A City (Tier 3) that supported 3 armies is captured. The kingdom still fields those 3 armies, but now they are **unsupported**.
- Each army must roll a Morale check at the start of the turn, likely causing unrest
- If the war drags on, penalties accumulate and the risk of losing armies rises sharply

---

## Example Kingdom Turn

**Kingdom:** 1 Town (Level 3, needs 4 Food)  
**Controlled hexes:**
- 2x Plains with Farmsteads = 4 Food
- 1x Forest with Logging Camp = 2 Lumber
- 1x Hills with Quarry = 1 Stone

### Turn Sequence:

**Phase 1 – Gain Fame:** 
- Start with 1 Fame (can spend to reroll kingdom checks)

**Phase 2 – Apply Ongoing Modifiers:** 
- Not at war (no unrest penalty)
- No special structure bonuses active
- Current Unrest: 2 (no penalty, remains under 5)

**Phase 3 – Check for Kingdom Events:** 
- Roll flat check DC 16: Rolled 14 (failure)
- No event this turn; DC drops to 11 for next turn

**Phase 4 – Manage Resources:**
- **Production:** 4 Food, 2 Lumber, 1 Stone
- **Food Consumption:** Town consumes 4 Food → balanced (no shortage/unrest)
- **Military Support:** 1 army active, Town supports 2 armies → no morale check needed
- **Construction Queue:** Building a Training Yard (costs 2 Lumber, 2 Stone total)
  - Apply 2 Lumber + 1 Stone this turn automatically
  - 1 Stone still needed to complete (will finish next turn)
- **Storage:** No Storehouses built → excess Lumber/Stone/Ore lost at end of turn
- **Gold:** No income this turn (no commerce structures)

**Phase 5 – Perform Kingdom Actions:**
- PC 1: **Develop Settlement** to add a Market Square (rolls success)
- PC 2: **Deal with Unrest** using Diplomacy (rolls success, -2 Unrest)
- Companions: **Send Scouts** to explore eastern hex (rolls success)

**Phase 6 – End of Turn Resolution:** 
- Unrest reduced to 0 (from the Deal with Unrest action)
- No lingering event effects
- Unused Lumber/Stone/Ore lost (no storage capacity)
- Gold balance remains at 3 (carried over)
- Training Yard will complete next turn when final Stone is produced

**Result:** Kingdom stable, construction progressing, Market Square added, eastern hex scouted.

---
