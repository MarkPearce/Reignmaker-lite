# Kingdom Rules

This document provides  details for kingdom management structures and economic systems.

---

## **Fame**

Fame represents your kingdom's reputation and notable achievements. It provides a mechanical benefit through rerolls and serves as a measure of your realm's growing influence.

### **Gaining Fame**

**Automatic Fame:**
- **Start of Turn:** Gain 1 Fame at the beginning of each Kingdom Turn (Phase 1)

**Earned Fame:**
- **Critical Success:** Gain 1 Fame when rolling a critical success on any kingdom action
- **Event Rewards:** Certain events grant Fame as a reward:
  - Archaeological Find (Critical Success)
  - Discovery (Critical Success)
  - Magical Discovery (Success option)
  - Pilgrimage (Critical Success)
  - Other events as specified

### **Using Fame**

**Reroll Kingdom Checks:**
- **Cost:** Spend 1 Fame to reroll any kingdom check
- **Timing:** Must decide to use Fame immediately after seeing the initial roll result
- **Limitation:** Can only reroll once per check (cannot spend multiple Fame on the same roll)
- **Must Take New Result:** You must use the second roll, even if it's worse

### **Fame Storage**

- Fame does not carry over between Kingdom Turns unless specifically noted
- There is no maximum Fame limit during a turn
- Unspent Fame is lost at the end of each Kingdom Turn

### **Example Fame Usage**

Your kingdom attempts to Deal with Unrest using Diplomacy:
1. Initial roll: Total of 8 (Failure)
2. Spend 1 Fame to reroll
3. New roll: Total of 15 (Success)
4. Must use the new result

This represents your kingdom leveraging its reputation and past achievements to overcome a difficult situation.

---

## **Unrest**

Unrest represents the dissatisfaction, tension, and disorder within your kingdom. It accumulates from various sources—failed actions, food shortages, unsupported armies, and unresolved events—and creates increasingly severe penalties as it builds.

### **Effects of Unrest**

Unrest imposes cumulative penalties on all kingdom actions:
- **0-3 Unrest:** No penalty
- **4-7 Unrest:** –1 status penalty to all kingdom rolls
- **8-11 Unrest:** –2 status penalty to all kingdom rolls
- **12-15 Unrest:** –3 status penalty to all kingdom rolls
- **16-19 Unrest:** –4 status penalty to all kingdom rolls
- **20-23 Unrest:** –5 status penalty to all kingdom rolls
- **24+ Unrest:** –6 status penalty to all kingdom rolls (and so on, -1 per 4 points)

### **Common Sources of Unrest**

**Failed Actions:**
- Critical failures on kingdom actions typically cause +1 or +2 Unrest
- Some regular failures may also generate +1 Unrest

**Resource Shortages:**
- Food shortage: +1 Unrest per missing Food each turn
- Unsupported armies: +1 Unrest per excess army each turn

**Military Issues:**
- Failed army morale checks: +1 Unrest (or +2 on critical failure)
- Army disbanding: +1 Unrest (or +2 if through mutiny/desertion)

**Other Sources:**
- Being at war: +1 Unrest per turn
- Unresolved kingdom events
- Certain narrative consequences

### **Imprisoned Unrest**

Imprisoned Unrest represents dissidents, troublemakers, and malcontents who have been detained by your justice system. This unrest is stored separately and does not count toward your kingdom's total Unrest penalties.

- **Storage:** Imprisoned Unrest is held in settlements with Justice structures (Courts, Tribunals, etc.)
- **Not Counted:** Does not contribute to kingdom roll penalties while imprisoned
- **Resolution:** Can be dealt with through the Execute or Pardon Prisoners action
- **Risk:** If not addressed, may escape or cause problems through events

### **Reducing Unrest**

**Direct Actions:**
- **Deal with Unrest** action (End of Turn only): Reduces 1-3 Unrest based on success
- **Execute or Pardon Prisoners**: Removes imprisoned Unrest (can also reduce current Unrest on critical success)

**Passive Reduction:**
- Certain structures automatically reduce Unrest each turn:
  - Theater (T3): –1 Unrest per turn
  - Grand Coliseum (T4): –1 Unrest per turn
  - Citadel (T4): –1 Unrest per turn
- Special events and critical successes may reduce Unrest

**Indirect Methods:**
- Maintaining adequate food supplies prevents Unrest from shortages
- Supporting all armies prevents military Unrest
- Resolving kingdom events prevents their lingering effects

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

### Road Network Bonus

**Connected Settlements:** Any settlement connected to another settlement by roads provides a **+1 circumstance bonus to all kingdom checks**. This bonus represents improved communication, trade, and administrative efficiency across your realm.

- Roads must form a continuous path between settlements
- Each connected settlement provides +1 (multiple connected settlements stack)
- Maximum bonus from road networks: +4
- Roads can be built with the Build Road action (see Kingdom Actions)

Example: If you have 5 settlements all connected by roads, you gain +4 to all kingdom checks.

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

### Structure Tier Progression (Upgrades)

Structures within the same category can be upgraded through tier progression. When you build a higher-tier structure in the same category as an existing lower-tier structure, you are upgrading that structure. The process works as follows:

**Upgrade Mechanics:**
- **Prerequisite:** Must have the lower-tier structure already built
- **Cost:** Pay the full resource cost of the higher-tier structure
- **Effect:** The lower-tier structure is replaced by the higher-tier version
- **Benefits:** The new structure provides all the enhanced benefits of its tier
- **Slot Usage:** The upgrade uses the same structure slot (no additional slot needed)

**Example Upgrade Chains:**
- Market (T1) → Marketplace (T2) → Grand Bazaar (T3) → Trade District (T4)
- Shrine (T1) → Temple (T2) → Cathedral (T3) → Grand Cathedral (T4)
- Workshop (T1) → Guild Hall (T2) → Artisan Quarter (T3) → Industrial Complex (T4)

**Important Notes:**
- You cannot skip tiers - must progress sequentially (T1→T2→T3→T4)
- Each tier requires the appropriate settlement size (Village for T1, Town for T2, etc.)
- The upgraded structure immediately provides its new tier's benefits
- Any bonuses or effects from the previous tier are replaced, not stacked

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

### Damaged & Destroyed Structures

Structures can be damaged or destroyed through events, warfare, or disasters. This creates meaningful consequences without completely devastating a settlement.

#### Damaged Structures
A damaged structure temporarily loses its benefits but can be repaired:

- **Status:** Structure provides no benefits while damaged
- **Settlement Level:** Still counts toward settlement structure limits
- **Repair Cost:** Half the original construction cost (rounded up)
- **Repair Time:** Resources applied normally through construction queue
- **Alternative:** Can be demolished (1 Kingdom Action) to free the slot

**Example:** A damaged Market (T1, originally 2 resources) requires 1 resource to repair.

#### Destroyed Structures
A destroyed structure is completely removed:

- **Status:** Structure and all benefits permanently lost
- **Settlement Level:** No longer counts toward structure limits
- **Rebuilding:** Must build from scratch using normal construction rules
- **Cascade Effects:** If destruction drops below tier requirements, settlement may need to adjust

**Special Cases:**
- If a settlement loses structures below its tier minimum (e.g., City with only 7 structures), it cannot advance levels until rebuilt
- Settlements never lose their tier status from structure loss alone
- Critical structures (like Granaries with stored food) lose their contents when destroyed

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

## Military

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

## **Diplomatic Relations**

Diplomatic relations represent your kingdom's standing with neighbouring realms, powerful factions, and influential organizations. These relationships directly impact trade opportunities, military alliances, and the overall stability of your borders. Each diplomatic relationship is tracked using an attitude scale that mirrors personal attitudes but operates at the kingdom level.

### **Attitude Levels**

Each faction, neighbouring kingdom, or major organization has an attitude toward your kingdom:

| Attitude | Description | Effects |
|----------|-------------|---------|
| **Helpful** | Actively supports your kingdom's interests | • may provide military aid if attacked<br>• Offers favourable trade deals (-1 Gold on purchases (min 1))<br>• May gift resources or share intelligence<br>• Allows military passage through their territory |
| **Friendly** | generally positive relationship | • Open to trade agreements<br>• Will consider military alliances<br>• Shares basic information and warnings<br>• -1 DC to diplomatic checks with this faction |
| **Indifferent** | No strong feelings either way | • Standard trade rates apply<br>• May be swayed to either side<br>• Neutral in conflicts<br>• Base DC for all diplomatic interactions |
| **Unfriendly** | Suspicious or hostile to your interests | • Trade restrictions (+1 Gold tax  on all purchases)<br>• +2 DC to diplomatic checks<br>• May support your enemies<br>• Closed borders to your armies |
| **Hostile** | Actively opposes your kingdom | • No trade permitted<br>• May declare war or raid borders<br>• +4 DC to diplomatic checks<br>• Provides aid to your enemies<br>• +1 Unrest per turn while hostile neighbor exists |

### **Diplomatic Capacity**

Maintaining close diplomatic relationships requires dedicated diplomatic infrastructure. Your kingdom's capacity for sustaining **Helpful** relationships is determined by your diplomatic structures:

**Calculating Capacity:**
- **No diplomatic structures:** 0 Helpful relationships (can still have Friendly or lower)
- **Sum all diplomatic structures in your kingdom:**
  - **Embassy (T2):** +1 Helpful relationship capacity
  - **Grand Embassy (T3):** +2 Helpful relationship capacity  
  - **Diplomatic Quarter (T4):** +3 Helpful relationship capacity

**Examples:**
- 2 Embassies = 2 Helpful relationships
- 1 Grand Embassy + 1 Embassy = 3 Helpful relationships
- 1 Diplomatic Quarter + 2 Grand Embassies = 7 Helpful relationships

**Exceeding Capacity:**
- You can have unlimited Friendly, Indifferent, Unfriendly, or Hostile relationships
- If you gain more Helpful relationships than your capacity (through events or critical successes), you must choose which to maintain at the end of the Kingdom Turn
- Relationships not maintained automatically degrade to Friendly
- Without any diplomatic structures, you cannot maintain Helpful relationships at all (they degrade to Friendly)

This represents the diplomatic corps, translators, administrative staff, and ongoing attention required to maintain the closest alliances. A kingdom that invests heavily in diplomatic infrastructure can expand its sphere of influence significantly.

### **Changing Attitudes**

Diplomatic attitudes can be shifted through kingdom actions, events, and consequences of your decisions:

**Improving Relations:**
- **Send Diplomatic Envoy** action (uses Diplomacy skill)
  - Success: Improve attitude by one step
  - Critical Success: Improve by one step + gain 1 Fame or reduce 1 Unrest
  - Failure: No change
  - Critical Failure: Worsen attitude by one step
- **Offer Tribute** (costs Gold or Resources based on faction power)
- **Complete faction requests or quests**
- **Supporting them in conflicts**

**Worsening Relations:**
- **Failed diplomatic attempts** (critical failures)
- **Breaking treaties or agreements**
- **Supporting their enemies**
- **Aggressive expansion near their borders**
- **Certain event choices**

### **Initial Attitudes**

When first encountering a new faction or kingdom, their initial attitude is typically **Indifferent** unless:
- **Historical grievances:** May start Unfriendly or Hostile
- **Shared culture/religion:** May start Friendly
- **Reputation effects:** Your kingdom's Fame or Infamy affects starting attitudes
- **Event outcomes:** Discovery circumstances may set initial attitude

### **Diplomatic Consequences**

**Multiple Hostile Neighbors:**
- Each Hostile faction: +1 Unrest per turn
- Risk of coordinated attacks increases
- Trade routes may be completely cut off

**Alliance Networks:**
- Helpful allies may intervene in wars
- Friendly kingdoms provide circumstance bonuses to stability
- Connected friendly kingdoms reduce event severity

**Trade Implications:**
- Helpful: -1 Gold per trade resource (min 1)
- Friendly: Standard rates
- Indifferent: Standard rates
- Unfriendly: +1 Gold tax per trade resource
- Hostile: No trade possible

### **Special Diplomatic Structures**

These structures from the Civic & Governance category enable and enhance diplomatic relations:

| Structure | Tier | Diplomatic Capacity | Additional Benefits |
|-----------|------|-------------------|-------------------|
| **Embassy** | T2 | 1 Helpful relationship | +1 circumstance bonus to diplomatic checks with one chosen faction |
| **Grand Embassy** | T3 | 2 Helpful relationships | +2 bonus with one faction, +1 with all others |
| **Diplomatic Quarter** | T4 | 3 Helpful relationships | +2 bonus to diplomatic checks with all factions |

**Note:** These structures also function as skill-based structures for earning income through Diplomacy, Society, and Deception skills.

---

## Kingdom Events

Kingdom events represent the unpredictable challenges and opportunities that arise as your realm grows. These events test your leaders' skills, create narrative moments, and can significantly impact your kingdom's development. Events occur randomly during the Kingdom Turn's event phase, requiring immediate attention and skillful resolution.

### Event Types

**Beneficial Events:** Generally positive events that provide opportunities for growth, wealth, or improved relations. Even beneficial events can have negative consequences if handled poorly.

**Dangerous Events:** Negative events that threaten the kingdom's stability, resources, or population. Successful resolution can sometimes turn these crises into opportunities.

**Continuous Events:** Events that persist across multiple turns until resolved. These ongoing situations require sustained effort and can escalate if ignored. Multiple continuous events can stack, potentially overwhelming an unprepared kingdom.

### Event Difficulty

All event skill checks use the **Level-based DC** for the party's level, following the standard kingdom rules. This ensures events remain challenging but manageable as the kingdom grows in power.

### Using Events in Play

**When Events Occur:**
During Phase 3 of each Kingdom Turn, check for events:
- **Base DC:** 16 (flat check)
- **Success:** An event occurs this turn
- **Failure:** No event; DC decreases by 5 (minimum DC 6)
- The DC resets to 16 after an event occurs

**Selecting an Event:**
When an event occurs, roll randomly from all available events. The GM should have a prepared list or table of all events appropriate for the campaign. Events can be:
- Rolled with equal probability
- Selected to fit the narrative when appropriate

**Multiple Events:** 
Continuous events persist alongside new events. The kingdom might face several ongoing crises simultaneously, creating complex strategic decisions about resource allocation and which problems to prioritize.

**Narrative Integration:** 
Events should tie into the campaign story when possible, reflecting consequences of player actions or foreshadowing future challenges. An assassination attempt might connect to a villain's broader schemes, while a diplomatic overture could open new storylines.

### Event Resolution

1. **Determine Location/Target:** Many events specify where they occur or whom they affect
2. **Choose Approach:** Players select which skill to use from the event's options
3. **Make the Check:** Roll using the appropriate PC's modifier
4. **Apply Results:** Implement the consequences based on degree of success
5. **Track Continuous Events:** Note any ongoing events for future turns

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
- Current Unrest: 2 (no penalty, remains under 4)

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
