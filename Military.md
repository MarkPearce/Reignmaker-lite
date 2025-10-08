# Military

Settlements provide the logistical foundation for supporting armies. This represents the infrastructure, supply lines, and population base needed to field and maintain armies. The military capacity of your kingdom determines how many armies you can sustain without straining your population and resources.

## Army Capacity and Support

Each settlement provides military support based on its tier. The kingdom's total army capacity is the sum of all settlements' individual capacities.

| Settlement Tier | Army Capacity |
|-----------------|---------------|
| Village (Tier 1) | 1 Army |
| Town (Tier 2)    | 2 Armies |
| City (Tier 3)    | 3 Armies |
| Metropolis (Tier 4) | 4 Armies |

**Army Food Consumption:**
- Each army requires **1 Food per turn** to maintain
- This is separate from and additional to settlement food consumption
- Army food shortages cause unrest exactly like settlement food shortages (+1 Unrest per missing Food)

**Exceeding Capacity:** If the kingdom fields more armies than its total military support capacity, each excess army increases **Unrest by 1 per Kingdom Turn**, reflecting the strain on the population and logistics.

**Structures and Modifiers:** Certain Structures (e.g., Barracks, Garrison, Fortress, Citadel) may enhance army support capacity. Unless specified, the baseline army capacity above applies.

## Loss of Military Support

If a settlement is **lost, destroyed, or captured**, its army capacity is immediately removed from the kingdom's total. If this causes the kingdom to exceed its military support capacity, the excess armies are considered **unsupported**.

### Unsupported Armies

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

### Example
A City (Tier 3) that supported 3 armies is captured. The kingdom still fields those 3 armies, but now they are **unsupported**.
- Each army must roll a Morale check at the start of the turn, likely causing unrest
- If the war drags on, penalties accumulate and the risk of losing armies rises sharply
