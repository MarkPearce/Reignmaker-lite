# Kingdom System Improvements

This document contains recommended improvements to make the kingdom-building system more enjoyable, inclusive, and less punishing while maintaining strategic depth.

## Core Design Philosophy
**FROM:** Punishing simulation where success gets harder as characters level up  
**TO:** Power fantasy where players build an empire and feel their growth makes them better leaders

---

## 1. Coordinated Effort Action (Replaces Provide Support)

### Coordinated Effort (Balanced Version)
_When two leaders work toward the same goal, their combined expertise ensures the best possible outcome._

**How it Works:**
- **Limit:** Maximum of TWO PCs may coordinate on the same action
- **Frequency:** May only be used ONCE per Kingdom Turn
- Both participating PCs roll the skill check for that action with a +1 circumstance bonus
- Take the highest result between the two participants
- The action succeeds using this best result

**Special Benefits:**
- No designated "lead" required - both participants are equal
- No risk of failure for coordination itself
- The +1 bonus represents teamwork and shared knowledge
- Other PCs must choose different actions, promoting diverse strategies
- Creates meaningful choice: which action is most important to coordinate?

**Example:**
```
PC1 and PC2 coordinate on "Build Roads" (the one coordinated action this turn)
- PC1 rolls Crafting: 1d20+8+1 = 16
- PC2 rolls Survival: 1d20+12+1 = 24  
- Result: The Build Roads action uses the 24
PC3 and Companion must choose different actions
```

**This change:**
- Removes the old "Provide Support" action entirely
- Eliminates risk of generating Unrest from failed support attempts
- Encourages strategic teamwork without making it the only optimal choice
- Maintains action diversity - not everyone doing the same thing
- Creates tactical decisions about when to use coordination

**Balance Impact:**
- **2 PCs Coordinating:** ~75% success chance (good but not guaranteed)
- **Forces Other Actions:** 2+ other PCs must act independently
- **Strategic Choice:** Must decide which action is most critical
- **Prevents Meta-Gaming:** Can't just coordinate everything

---

## 2. Inclusive Skill System

### Allow Substitution Skills
Instead of rigid skill requirements, let players use their best skills creatively:

**Create Worksite:**
- PRIMARY: Survival or Nature
- ALTERNATIVES: 
  - Crafting (building infrastructure)
  - Athletics (physical labor)
  - Society (organizing work crews)
  - Intimidation (forcing prisoners to work)

**Deal with Unrest:**
- PRIMARY: Diplomacy
- ALTERNATIVES:
  - Performance (entertainment)
  - Religion (sermons)
  - Intimidation (iron fist)
  - Deception (propaganda)
  - Athletics (public games)
  - Arcana (magical displays)

**Claim Hexes:**
- PRIMARY: Nature or Survival
- ALTERNATIVES:
  - Warfare Lore (military conquest)
  - Diplomacy (peaceful annexation)
  - Intimidation (forcing submission)
  - Society (cultural expansion)

### Party Skill Pooling
- **Assist Another:** +2 circumstance bonus if another PC is trained in the skill
- **Skill Synergy:** If 2+ PCs are trained in relevant skills, +1 additional bonus
- **Specialization Bonus:** The PC with highest modifier rolls, others can assist

---

## 3. Kingdom Experience System

The kingdom itself gains "experience" separate from party level:

### Kingdom Level Progression
- Starts at 1
- Increases by 1 every 5 sessions (or at milestone achievements)
- Provides bonus to ALL kingdom checks: +Kingdom Level
- At Kingdom Level 5, 10, 15: Gain a Kingdom Feat

### Infrastructure Bonuses
Completed structures provide cumulative bonuses:
- Every 5 structures built: +1 to all kingdom checks
- Every 10 hexes with roads: +1 to all kingdom checks
- Every settlement upgraded: +1 to all kingdom checks in that region
- Every 25 hexes controlled: +1 to all kingdom checks

### Kingdom Feats (Choose at Kingdom Level 5, 10, 15)
- **Agricultural Mastery:** All farms produce +1 Food
- **Defensive Architecture:** All fortifications provide +2 AC instead of +1
- **Trade Empire:** Improve all trade ratios by 1 step
- **Cultural Renaissance:** -2 Unrest at end of each session
- **Military Tradition:** All recruited units start at +1 level
- **Magical Kingdom:** Can use Arcana/Occultism for ANY kingdom action
- **Diplomatic Excellence:** +2 to all Foreign Affairs actions
- **Industrial Revolution:** All worksites produce +1 resource every 3rd turn
- **Educational System:** All skill-based structures provide additional +1 bonus

---

## 4. Reduced Punishment Severity

### Unrest Soft Cap System
**OLD:** Unrest provides -1 per 5 (unlimited)

**NEW:**
- Unrest 1-5: No penalty
- Unrest 6-10: -1 penalty
- Unrest 11-15: -2 penalty  
- Unrest 16-20: -3 penalty
- Unrest 21+: -3 penalty (CAPPED) + special narrative events

### Failure Mitigation
Regular failures no longer automatically generate Unrest:

**Degrees of Failure:**
- Fail by 1-2: **Partial Success** (half effect, no Unrest)
- Fail by 3-4: **No Progress** (action fails, no Unrest)
- Fail by 5+: **Setback** (+1 Unrest)
- Critical Failure: **Major Setback** (+2 Unrest)

### Recovery Mechanisms
- **Natural Unrest Decay:** -1 Unrest per session automatically
- **Fame Usage Expanded:** Spend 1 Fame to reduce Unrest by 2 (not just reroll)
- **Rest & Celebration:** Skip all kingdom actions for one turn to reduce Unrest by 3
- **Cultural Events:** Certain structures reduce Unrest at start of each turn

---

## 5. DC Scaling Solutions

### Option A: Flat DC System
Kingdom actions use STATIC DCs regardless of party level:
- Easy Tasks: DC 15
- Moderate Tasks: DC 20  
- Hard Tasks: DC 25
- Extreme Tasks: DC 30

### Option B: Bounded Progression (Recommended)
Kingdom DCs = 14 + (Party Level/2), rounded down
- Level 4: DC 16
- Level 8: DC 18
- Level 12: DC 20
- Level 16: DC 22
- Level 20: DC 24

### Option C: Advantage System
Certain conditions grant Advantage on kingdom rolls:
- Acting from Capital
- Relevant structure in settlement
- Kingdom is Prosperous (no Unrest, all settlements fed)
- Diplomatic allies assisting
- Kingdom Level bonus applies

---

## 6. Resource System Improvements

### Resource Banking
**Basic Storage (no structure needed):**
- 25% of resources carry over to next turn
- With T1 Storage: 50% carry over
- With T2 Storage: 75% carry over
- With T3+ Storage: 100% carry over

### Emergency Reserves
- Can "deficit spend" up to 5 resources
- Must be repaid within 3 turns
- Each turn in deficit: Roll DC 15 flat check or +1 Unrest

### Flexible Production
Worksites can "flex" production once per session:
- Farmstead → Can produce 1 Lumber instead of 2 Food
- Logging Camp → Can produce 1 Food (hunting) instead of 2 Lumber
- Quarry → Can produce 1 Ore instead of 1 Stone
- Mine → Can produce emergency Gold (1 Gold instead of 1 Ore)

### Improved Trade Ratios
**Base Rates:**
- Purchase: 3 Gold → 2 Resources (improved from 2:1)
- Sell: 3 Resources → 2 Gold (improved from 2:1)

---

## 7. Event System Rework

### Positive Events (20% chance)
- **Merchant Caravan:** Free 2d4 resources of chosen type
- **Bumper Harvest:** +50% food production this turn
- **Diplomatic Gift:** +1d6+2 Gold from neighboring kingdom
- **Refugees:** Free settlement upgrade or +1d4 trained workers
- **Discovery:** Find special resource or ancient structure
- **Hero's Return:** Reduce Unrest by 1d4

### Neutral Events (40% chance)
Present choices without automatic negative consequences

### Player Choice Events
Instead of pass/fail, give meaningful choices:

**"Bandit Demands"**
- Option A: Pay 5 Gold (no check needed)
- Option B: Military response (Combat encounter)
- Option C: Negotiate (Diplomacy DC 20 for peaceful resolution)
- Option D: Ignore them (+2 Unrest, may attack in 1d4 turns)

### Narrative Failures
Even failed rolls can create story opportunities:
- Failed "Create Worksite": "You establish the mine, but discover it's haunted - new quest available!"
- Failed "Establish Settlement": "The settlement is founded but immediately needs help with local monsters"

---

## 8. Hero Point Integration

Allow Hero Points on Kingdom Rolls:
- Spend 1 Hero Point: Reroll any kingdom check
- Spend 2 Hero Points: Automatically succeed on a kingdom check
- Spend 3 Hero Points: Critical success on a kingdom check

---

## 9. Quick Win Opportunities

### Session Rewards
Completing any session provides (choose one):
- +1 Kingdom XP
- 2 Gold to treasury
- 4 Resources of any single type
- -1 Unrest
- +1 Fame

### Milestone Bonuses
- **First Town:** All PCs gain +1 to kingdom checks permanently
- **First City:** Kingdom gains resistance to Unrest (half penalties)
- **First Metropolis:** Kingdom actions can't critically fail
- **10 Settlements:** Double Fame generation
- **50 Hexes:** +5 to all kingdom checks
- **100 Hexes:** Legendary kingdom status (special benefits)

---

## 10. Additional Quality of Life Improvements

### Cooperative Actions
**New Action: Combined Effort**
- All PCs work together on single major task
- Roll with highest modifier +2 per additional PC
- Success grants enhanced effect
- Failure has reduced penalty (no Unrest on regular failure)

### Building Completion Bonuses
When a structure is completed:
- Immediate -1 Unrest (citizens celebrate)
- Gain 1 Fame if it's the first of its type in the kingdom
- Structures provide immediate benefits (don't wait until next turn)

### Settlement Specialization
Settlements can declare a specialization once they reach Town size:
- **Trade Hub:** +1 Gold per turn, better conversion rates
- **Military Fort:** +2 unit capacity, units recruit at +1 level
- **Agricultural Center:** +2 Food production in surrounding hexes
- **Industrial Center:** -1 resource cost for all structures
- **Cultural Center:** -1 Unrest per turn, +1 Fame generation

---

## Implementation Priority

### Phase 1 (Immediate - Fix Core Issues)
1. Implement new Provide Support action
2. Change failure results (remove automatic Unrest)
3. Add Kingdom Level system
4. Implement bounded DC progression

### Phase 2 (Soon - Add Depth)
1. Add skill substitutions
2. Implement resource banking
3. Add positive events
4. Create Kingdom Feats

### Phase 3 (Later - Polish)
1. Add settlement specializations
2. Implement milestone bonuses
3. Create narrative failure system
4. Add Hero Point integration

---

## Expected Outcomes

With these changes:
- **Success Rate:** Increases from 47% to approximately 65-70%
- **Unrest Management:** Reduced from 36% of actions to ~10%
- **Player Engagement:** All character types can meaningfully contribute
- **Progression Feel:** Kingdom gets stronger over time, not weaker
- **Fun Factor:** Collaboration rewarded, failures create opportunities
- **Strategic Depth:** More choices, fewer forced responses to crises

The system transforms from a grinding survival challenge into an engaging empire-building experience where players feel empowered to shape their kingdom's destiny.
