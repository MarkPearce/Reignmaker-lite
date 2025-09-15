# Kingdom Events Complete Audit
_Comprehensive analysis of Kingdom Events against core game systems_

## Executive Summary

This audit examines all 40 kingdom events for:
1. **System Alignment** - Integration with kingdom rules and mechanics
2. **Skill Availability** - Whether required skills exist in kingdom actions
3. **Balance & Fun** - Resource scales, risk/reward, and player engagement

---

## SECTION 1: SKILL AVAILABILITY ANALYSIS

### Core Kingdom Skills (Available through Kingdom Actions)
These skills appear in Kingdom Actions and are readily available to players:
- **Diplomacy** (11 actions)
- **Society** (9 actions)
- **Intimidation** (8 actions)
- **Survival** (5 actions)
- **Nature** (5 actions)
- **Crafting** (5 actions)
- **Medicine** (2 actions)
- **Performance** (2 actions)
- **Religion** (1 action)
- **Warfare Lore** (6 actions)
- **Mercantile Lore** (2 actions)
- **Intrigue Lore** (1 action)

### Problematic Skills in Events
These skills appear in events but NOT in any Kingdom Actions:

#### **Critical Issues (No Kingdom Action Access)**
| Skill | Events Using It | Problem |
|-------|----------------|---------|
| **Stealth** | 8 events | Zero kingdom actions use this |
| **Thievery** | 3 events | Zero kingdom actions use this |
| **Deception** | 5 events | Zero kingdom actions use this |
| **Arcana** | 4 events | Zero kingdom actions use this |
| **Occultism** | 3 events | Zero kingdom actions use this |
| **Athletics** | 2 events | Zero kingdom actions use this |
| **Acrobatics** | 2 events | Zero kingdom actions use this |
| **Lore** | 1 event | Zero kingdom actions use this (only specific Lores) |

### Event-by-Event Skill Problems

#### Events with Unavailable Skills:
1. **Archaeological Find** - Occultism (unavailable)
2. **Assassination Attempt** - Stealth (unavailable)
3. **Bandit Activity** - Stealth (unavailable)
4. **Cult Activity** - Stealth (unavailable)
5. **Diplomatic Overture** - Deception (unavailable)
6. **Drug Den** - Stealth (unavailable)
7. **Feud** - Deception (unavailable)
8. **Grand Tournament** - Athletics, Acrobatics (both unavailable)
9. **Infiltration** - Deception, Stealth, Thievery (all unavailable in actions)
10. **Magical Discovery** - Arcana, Occultism (both unavailable)
11. **Military Exercises** - Athletics, Acrobatics (both unavailable)
12. **Monster Attack** - Stealth (unavailable)
13. **Notorious Heist** - Thievery, Stealth (both unavailable)
14. **Sensational Crime** - Uses Society (available)
15. **Scholarly Discovery** - Lore, Arcana (both unavailable)
16. **Trade Agreement** - Deception (unavailable)
17. **Undead Uprising** - Arcana (unavailable)

---

## SECTION 2: STRUCTURAL MECHANICS ISSUES

### Structure Bonus System - CORRECTED UNDERSTANDING

**Events provide UNTYPED bonuses** (which stack with other bonuses)
**Structures provide CIRCUMSTANCE bonuses** (which don't stack with each other)

This is actually correct design - events check for the presence of structures and grant untyped bonuses based on their tier:
- T1: +1 untyped bonus from events
- T2: +2 untyped bonus from events
- T3: +3 untyped bonus from events  
- T4: +4 untyped bonus from events

The structure's own circumstance bonuses (+1/+2/+3) are separate and apply to earn income actions.

**Current Event Language is Correct:**
Events properly state "gain an untyped bonus equal to the tier" - this is intentional to allow stacking with other bonuses. No changes needed to event bonus language.

### Structure Category References

Most events correctly reference structure categories, with minor clarifications needed:
- Events say "Performance & Culture" - should clarify if this means Performance skill structures OR Culture support structures
- Events say "Knowledge & Magic" which correctly matches the skill structure category
- Events say "Faith & Nature" which correctly matches the skill structure category
- Events say "Crime & Intrigue" which correctly matches the skill structure category

---

## SECTION 3: RESOURCE & BALANCE ISSUES

### Overly Punishing Events

#### **Food Shortage**
- **Problem**: Losing 6-8 Food per turn can instantly starve a small kingdom
- **Context**: A Village needs 1 Food, Town needs 4 Food
- **Fix Needed**: Scale to kingdom size (e.g., lose 50% of Food production)

#### **Natural Disaster**  
- **Problem**: Can destroy ALL worksites in 3 hexes
- **Context**: Worksites cost actions to build and are core economy
- **Fix Needed**: Damage worksites, don't destroy; limit to 1 worksite per hex

#### **Raiders (Continuous)**
- **Problem**: -2 Gold, -2 Food per turn is devastating
- **Context**: Small kingdoms may only produce 2-4 Food total
- **Fix Needed**: Scale losses or make it -1 Gold, -1 Food

#### **Plague (Continuous)**
- **Problem**: -2 Gold per turn plus spreading is too harsh
- **Context**: Can cascade across entire kingdom via roads
- **Fix Needed**: Remove Gold loss or reduce spread chance

### Overly Generous Events

#### **Land Rush**
- **Problem**: Gaining 1-2 free hexes is massive (normally costs a full Kingdom Action)
- **Fix Needed**: Grant 1 hex maximum, or give bonus to next Claim Hex action

#### **Magical Discovery**
- **Problem**: Free structure or upgrade worth 8-18 resources
- **Fix Needed**: Discount on next magical structure instead

#### **Remarkable Treasure**
- **Problem**: +4 Gold on critical success is huge for early game
- **Fix Needed**: Cap at +3 Gold or scale to kingdom size

---

## SECTION 4: MISSING GAME MECHANICS

### Undefined or Inconsistent Mechanics

1. **"Convert X Unrest to imprisoned Unrest"** (Drug Den, Notorious Heist)
   - This happens without using the Arrest Dissidents action
   - No capacity check mentioned

2. **Structure Damage/Destruction**
   - Referenced in 12+ events but no repair rules in main system
   - Repair costs mentioned as "half original" but not in core rules

3. **Fame Persistence**
   - Events grant Fame but rules say Fame resets each turn
   - Should these be permanent Fame or just for current turn?

4. **PC Targeting**
   - "Random PC" mechanism not defined
   - What if PC is absent/dead?

5. **Hex Selection**
   - "Random hex" selection method not defined
   - "Random settlement" selection not defined

---

## SECTION 5: THEMATIC & GAMEPLAY ANALYSIS

### What Works Well

1. **Choice Variety** - Most events offer 2-3 skill approaches
2. **Continuous Events** - Create ongoing narrative pressure
3. **Risk/Reward Balance** - Beneficial events can fail, dangerous can succeed
4. **Diverse Themes** - Political, economic, military, supernatural variety

### What's Missing

1. **No Road Network Events** - Roads are major investment but no events interact
2. **No Diplomatic Relationship Events** - System tracks relationships but events don't use them
3. **No Structure-Specific Events** - Could have events for specific structures
4. **No Seasonal Events** - No weather/harvest cycle
5. **Limited PC Integration** - Only 3 events target specific PCs

### Repetitive Consequences

Too many events use "+1/+2 Unrest" as the failure state. Consider alternatives:
- Temporary structure shutdown
- Resource production penalties  
- Diplomatic reputation effects
- Movement restrictions
- Temporary skill penalties

---

## SECTION 6: SPECIFIC EVENT RECOMMENDATIONS

### Priority 1: Events Requiring Immediate Fixes

#### **Events with Completely Unavailable Skills** (17 events)
These MUST be fixed for the system to function:

1. **Archaeological Find**
   - Replace Occultism → Religion or Nature

2. **Assassination Attempt**  
   - Replace Stealth → Survival (evading) or Society (intelligence network)

3. **Bandit Activity**
   - Replace Stealth → Survival or Nature (tracking)

4. **Cult Activity**
   - Replace Stealth → Society or Survival

5. **Diplomatic Overture**
   - Replace Deception → Diplomacy (already an option)

6. **Drug Den**
   - Replace Stealth → Society or Survival

7. **Feud**
   - Replace Deception → Society or Performance

8. **Grand Tournament**
   - Replace Athletics → Intimidation or Warfare Lore
   - Replace Acrobatics → Performance or Diplomacy

9. **Magical Discovery**
   - Replace Arcana → Religion or Nature
   - Replace Occultism → Society or Medicine

10. **Military Exercises**
    - Replace Athletics → Intimidation or Warfare Lore
    - Replace Acrobatics → Survival or Nature

11. **Monster Attack**
    - Replace Stealth → Survival (already has Nature option)

12. **Notorious Heist**
    - Replace Thievery → Society or Intrigue Lore
    - Replace Stealth → Survival or Nature

13. **Scholarly Discovery**
    - Replace Lore → Society or Diplomacy
    - Replace Arcana → Religion or Medicine

14. **Trade Agreement**
    - Replace Deception → Mercantile Lore or Crafting

15. **Undead Uprising**
    - Replace Arcana → Medicine or Nature

16. **Infiltration** (Kingdom Action)
    - Already has this issue noted in Kingdom Actions
    - Replace with Society, Intrigue Lore, or Diplomacy options

### Priority 2: Balance Adjustments

#### **Scaling Fixes Required**

**Food Shortage**
```
Current: Lose 2/4/6/8 Food (flat)
Suggested: Lose 25%/50%/75%/100% of Food production
```

**Natural Disaster**
```
Current: Can destroy all worksites in 3 hexes
Suggested: Damages (not destroys) 1 worksite per hex, settlements get separate save
```

**Raiders**
```
Current: -2 Gold, -2 Food per turn
Suggested: -1 Gold OR -1 Food (choose one) per turn
```

### Priority 3: Structure Bonus Language Clarification

The current event language is CORRECT. Events should continue to use:
```
"If you have [Structure Category] structures, gain an untyped bonus 
equal to the tier of the structure"
```

This is intentional design - untyped bonuses from events stack with circumstance bonuses from structures and other sources.

---

## SECTION 7: IMPLEMENTATION CHECKLIST

### Immediate Actions Required
- [ ] Replace all unavailable skills in 17 events
- [ ] Add scaling to resource loss events (4 events)
- [ ] Define repair mechanics for damaged structures
- [ ] Clarify Fame persistence from events
- [ ] Add "random selection" tables for hexes/settlements/PCs

### System Additions Recommended
- [ ] Add Stealth skill to 1-2 Kingdom Actions (perhaps Infiltration)
- [ ] Add Deception skill to 1-2 Kingdom Actions
- [ ] Consider adding Investigation/Detective type action using multiple skills
- [ ] Create repair structure action for damaged buildings

### New Events to Consider
- [ ] Road network completion bonus event
- [ ] Diplomatic relationship change events
- [ ] Structure-specific events (e.g., "University Discovery" for Knowledge structures)
- [ ] Seasonal/weather cycle events
- [ ] Trade route establishment events

---

## SECTION 8: FUN FACTOR ANALYSIS

### High Engagement Events (Keep As-Is)
1. **Festive Invitation** - Interesting resource gamble mechanic
2. **Immigration** - Clear benefits, good risk/reward
3. **Visiting Celebrity** - Simple but flavorful
4. **Archaeological Find** - Good variety of outcomes
5. **Good Weather** - Continuous benefit that can end

### Low Engagement Events (Need Improvement)
1. **Demand Structure** - Too binary (build or suffer)
2. **Demand Expansion** - Too similar to Demand Structure
3. **Public Scandal** - Minimal interesting choices
4. **Local Disaster** - Pure negative, no upside potential
5. **Execute or Pardon Prisoners** - Mechanical, lacks narrative

### Suggested Improvements for Low Engagement Events

**Demand Structure** → "Development Petition"
- Citizens request specific structure type
- Success: They help fund it (reduced cost)
- Failure: Normal cost but must build within 2 turns

**Public Scandal** → "Political Intrigue"  
- Choose: Cover up (risky), Confess (costly), or Investigate (time-consuming)
- Each path has different skill checks and outcomes

---

## CONCLUSIONS

### System Viability
The event system is **fundamentally sound** but requires **significant skill adjustments** to function with the current Kingdom Actions. 17 of 40 events (42.5%) use skills that players cannot develop through kingdom play.

### Balance Assessment  
Resource losses need **scaling mechanics** rather than flat values. Several events are too punishing for small kingdoms while being trivial for large ones.

### Fun Factor
The variety and narrative potential are **strong**. The main issues are mechanical (skill availability) rather than conceptual. Once skills are aligned, this system will provide excellent gameplay variety.

### Priority Fixes
1. **Replace unavailable skills** (Critical - system doesn't function without this)
2. **Scale resource losses** (High - prevents kingdom death spirals)
3. **Define missing mechanics** (Medium - repair rules, random selection, etc.)
4. **Add missing events** (Low - enhancement rather than fix)

---

_Audit Complete - Date: 9/15/2025_
