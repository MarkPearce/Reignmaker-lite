# Settlements

Settlements are the heart of your kingdom, representing population centers that drive growth, cultural development, and military power. From humble villages to sprawling metropolises, each settlement serves as a hub for resource consumption, structure construction, and army support. As settlements grow in size and sophistication, they unlock access to more advanced structures, support larger military forces, and become centers of specialized knowledge and industry. The careful development and protection of settlements forms the cornerstone of any successful kingdom's strategy.

## Road Network Bonus

**Connected Settlements:** Any settlement connected to another settlement by roads provides a **+1 circumstance bonus to all kingdom checks**. This bonus represents improved communication, trade, and administrative efficiency across your realm.

- Roads must form a continuous path between settlements
- Each connected settlement provides +1 (multiple connected settlements stack)
- Maximum bonus from road networks: +4
- Roads can be built with the Build Road action (see Kingdom_Actions.md)

Example: If you have 5 settlements all connected by roads, you gain +4 to all kingdom checks.

## Settlement Levels & Structure Limits

Settlement advancement is gated by both **level thresholds** and **structure prerequisites**.
To advance to the next tier of settlement, you must:
1. First reach the **maximum number of structures** for your current tier
2. Then promote your settlement level to the minimum threshold of the next tier

| Settlement | Tier       | Food/Turn | Level Range | Max Structures | Advancement Requirement |
|------------|-------------|----------------|-----------------------------|-----------------------------|--------------------------------|
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

## Settlement Gold Generation

Settlements that are properly supported with food generate wealth for the kingdom through taxes, trade, and economic activity.

**Gold Generation:** A settlement which is properly supported with food earns its tier level in gold each turn.

| Settlement | Tier | Gold/Turn (when fed) |
|------------|------|---------------------|
| Village | 1 | 1 Gold |
| Town | 2 | 2 Gold |
| City | 3 | 3 Gold |
| Metropolis | 4 | 4 Gold |

**Important:** Settlements experiencing food shortages do not generate gold that turn, as the population focuses on survival rather than economic activity.
