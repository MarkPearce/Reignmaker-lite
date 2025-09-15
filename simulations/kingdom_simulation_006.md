# Kingdom Simulation #006 - Enhanced Hex-Based Unrest System

**Date:** September 15, 2025  
**Simulation Seed:** 20250915-183000
**Runner:** AI Assistant
**Rule Variants:** 
- Standard critical failure rules (+1 Unrest on all crit fails)
- **NEW UNREST SYSTEM:**
  - **Hex-based:** +1 Unrest per 8 hexes controlled (per turn)
  - **Metropolis:** +1 additional Unrest per turn
  - **Culture buildings:** Only provide bonuses (except Auditorium -1/turn)
**Result:** [To be determined]

## Unrest Mechanics for This Simulation

### Passive Unrest Generation
- **8-15 hexes:** +1 Unrest per turn
- **16-23 hexes:** +2 Unrest per turn
- **24-31 hexes:** +3 Unrest per turn
- **32+ hexes:** +4 Unrest per turn
- **Each Metropolis:** +1 Unrest per turn (additional)

### Unrest Management
- **Open Stage (T1):** +1 to Deal with Unrest checks
- **Amphitheater (T2):** +2 to Deal with Unrest checks
- **Playhouse (T3):** +2 to Deal with Unrest checks
- **Auditorium (T4):** -1 Unrest per turn + +2 to checks
- **Deal with Unrest:** Success = -2, Crit = -3, Fail = -1, Crit Fail = 0
- **Arrest Dissidents:** Convert unrest to imprisoned (2 on success, 4 on crit)

---

## Initial Statistics (Turn 0)

Standard starting conditions (Village Level 0, 3 hexes, no structures, etc.)

---

## Turn 1 - Party Level 4 (DC 19)

### Phase 1: Gain Fame
- Starting Fame: 1
- Gained: +1
- Total: 2

### Phase 2: Apply Modifiers
- Passive Unrest: 0 (only 3 hexes)
- Current Unrest: 0

### Phase 3: Kingdom Event
- DC: 16
- Roll: 10
- Event: None

### Phase 4: Resources
- Food: 0 (no production)
- Consumption: -1 (Village)
- Net: -1 (deficit!)

### Phase 5: Kingdom Actions
1. PC1 (Expert +11): Create Worksite (Plains - Farmstead)
   - Roll: 14+11 = 25 vs DC 19
   - Result: Success
   - Effect: Farmstead created

2. PC2 (Expert +11): Build Structure (Granary)
   - Roll: 11+11 = 22 vs DC 19
   - Result: Success
   - Effect: Granary built (+12 food storage)

3. PC3 (Trained +8): Claim Hex
   - Roll: 16+8 = 24 vs DC 19
   - Result: Success
   - Effect: 1 hex claimed (4 total)

4. PC4 (Trained +8): Create Worksite (Forest - Lumbermill)
   - Roll: 9+8 = 17 vs DC 19
   - Result: Failure
   - Effect: No worksite

5. Companions (+6): Build Roads
   - Roll: 13+6 = 19 vs DC 19
   - Result: Success
   - Effect: Roads built

### Phase 6: Summary
- Hexes: 4
- Unrest: 0 (no passive generation yet)
- Food secured with farmstead

---

## Turn 2 - Party Level 4 (DC 19)

### Phase 1: Gain Fame
- Total: 3

### Phase 2: Apply Modifiers
- Passive Unrest: 0 (only 4 hexes)
- Current Unrest: 0

### Phase 3: Kingdom Event
- DC: 11
- Roll: 7
- Event: None

### Phase 4: Resources
- Food Production: +2 (Farmstead)
- Consumption: -1
- Net: +1
- Storage: 1/24

### Phase 5: Kingdom Actions
1. PC1 (Expert +11): Upgrade Settlement
   - Roll: 12+11 = 23 vs DC 19
   - Result: Success
   - Effect: Village → Level 1

2. PC2 (Expert +11): Create Worksite (Forest - Lumbermill)
   - Roll: 8+11 = 19 vs DC 19
   - Result: Success
   - Effect: Lumbermill created

3. PC3 (Trained +8): Claim Hex
   - Roll: 11+8 = 19 vs DC 19
   - Result: Success
   - Effect: 1 hex claimed (5 total)

4. PC4 (Trained +8): Build Structure (Open Stage)
   - Roll: 3+8 = 11 vs DC 19
   - Result: Failure
   - Effect: No structure

5. Companions (+6): Claim Hex
   - Roll: 14+6 = 20 vs DC 19
   - Result: Success
   - Effect: 1 hex claimed (6 total)

### Phase 6: Summary
- Hexes: 6
- Unrest: 0
- Good expansion pace

---

## Turn 3 - Party Level 4 (DC 19)

### Phase 1: Gain Fame
- Total: 4

### Phase 2: Apply Modifiers
- Passive Unrest: 0 (6 hexes, threshold is 8)
- Current Unrest: 0

### Phase 3: Kingdom Event
- DC: 6
- Roll: 18
- Event: **Merchant Caravan** (+3 Gold)

### Phase 4: Resources
- Food: +2
- Lumber: +1
- Consumption: -1
- Gold: 3

### Phase 5: Kingdom Actions
1. PC1 (Expert +11): Trade with Merchants
   - Roll: 16+11 = 27 vs DC 19
   - Result: Success
   - Effect: +2 Gold (total: 5)

2. PC2 (Expert +11): Build Structure (Open Stage)
   - Roll: 10+11 = 21 vs DC 19
   - Result: Success
   - Effect: Open Stage built (+1 to unrest checks)

3. PC3 (Trained +8): Create Worksite (Hills - Quarry)
   - Roll: 13+8 = 21 vs DC 19
   - Result: Success
   - Effect: Quarry created

4. PC4 (Trained +8): Claim Hex
   - Roll: 15+8 = 23 vs DC 19
   - Result: Success
   - Effect: 1 hex claimed (7 total)

5. Companions (+6): Upgrade Settlement
   - Roll: 1+6 = 7 vs DC 19
   - Result: Critical Failure! (fails by 12)
   - Effect: No upgrade, +1 Unrest

### Phase 6: Summary
- Hexes: 7
- Unrest: 1 (first unrest from crit fail)
- Almost at 8 hex threshold

---

## Turn 4 - Party Level 4 (DC 19)

### Phase 1: Gain Fame
- Total: 5

### Phase 2: Apply Modifiers
- Passive Unrest: 0 (7 hexes)
- Current Unrest: 1

### Phase 3: Kingdom Event
- DC: 16
- Roll: 5
- Event: None

### Phase 4: Resources
- Food: +2, Lumber: +1, Stone: +1
- Consumption: -1
- Net positive

### Phase 5: Kingdom Actions
1. PC1 (Expert +11): Claim Hex
   - Roll: 20+11 = 31 vs DC 19
   - Result: Critical Success! (beats by 12)
   - Effect: 2 hexes claimed (9 total)
   - **WARNING: Now at 9 hexes, passive unrest starts next turn!**

2. PC2 (Expert +11): Upgrade Settlement
   - Roll: 14+11 = 25 vs DC 19
   - Result: Success
   - Effect: Village Level 1 → Level 2 (Town!)

3. PC3 (Trained +8): Build Structure (Marketplace)
   - Roll: 10+8 = 18 vs DC 19
   - Result: Failure
   - Effect: No structure

4. PC4 (Trained +8): Deal with Unrest
   - Roll: 17+8 = 25 vs DC 19
   - Result: Success
   - Effect: -2 Unrest (down to 0, with +1 from Open Stage bonus factored in)

5. Companions (+6): Recruit Army
   - Roll: 11+6 = 17 vs DC 19
   - Result: Failure
   - Effect: No army

### Phase 6: Summary
- Hexes: 9 (passive unrest triggered!)
- Settlement: Town Level 2
- Unrest: 0 (managed for now)

---

## Turn 5 - Party Level 5 (DC 20)

### Phase 1: Gain Fame
- Total: 6

### Phase 2: Apply Modifiers
- **Passive Unrest: +1 (9 hexes = 8-15 range)**
- Starting Unrest: 0
- New Unrest: 1

### Phase 3: Kingdom Event
- DC: 11
- Roll: 14
- Event: **Bandit Activity**

### Phase 4: Resources
- Food: +2
- Consumption: -2 (Town)
- Net: 0 (balanced)

### Phase 5: Kingdom Actions
1. PC1 (Expert +12): Resolve Bandit Event
   - Roll: 9+12 = 21 vs DC 20
   - Result: Success
   - Effect: Bandits driven off

2. PC2 (Expert +12): Build Structure (Stocks - T1 Justice)
   - Roll: 15+12 = 27 vs DC 20
   - Result: Success
   - Effect: Stocks built (can hold 1 imprisoned unrest)

3. PC3 (Trained +9): Create Worksite (Second Farm)
   - Roll: 11+9 = 20 vs DC 20
   - Result: Success
   - Effect: Second farmstead created

4. PC4 (Trained +9): Claim Hex
   - Roll: 8+9 = 17 vs DC 20
   - Result: Failure
   - Effect: No hex

5. Companions (+7): Deal with Unrest
   - Roll: 16+7 = 23 vs DC 20
   - Result: Success
   - Effect: -2 Unrest (but +1 from Open Stage already counted)
   - Unrest: 0

### Phase 6: Summary
- Hexes: 9
- Unrest: 0 (but will gain +1 next turn)
- Justice infrastructure started

---

## Turn 6 - Party Level 5 (DC 20)

### Phase 1: Gain Fame
- Total: 7

### Phase 2: Apply Modifiers
- Passive Unrest: +1 (9 hexes)
- Starting: 0
- New: 1

### Phase 3: Kingdom Event
- DC: 16
- Roll: 3
- Event: None

### Phase 4: Resources
- Food: +4 (2 farms)
- Consumption: -2
- Net: +2

### Phase 5: Kingdom Actions
1. PC1 (Expert +12): Arrest Dissidents
   - Roll: 12+12 = 24 vs DC 20
   - Result: Success
   - Effect: Convert 2 Unrest → imprisoned (but only 1 available)
   - Imprisoned: 1, Regular: 0

2. PC2 (Expert +12): Build Structure (Barracks)
   - Roll: 7+12 = 19 vs DC 20
   - Result: Failure
   - Effect: No structure

3. PC3 (Trained +9): Claim Hex
   - Roll: 19+9 = 28 vs DC 20
   - Result: Success
   - Effect: 1 hex claimed (10 total)

4. PC4 (Trained +9): Recruit Army
   - Roll: 2+9 = 11 vs DC 20
   - Result: Critical Failure! (fails by 9)
   - Effect: No army, +1 Unrest

5. Companions (+7): Build Structure (Marketplace)
   - Roll: 14+7 = 21 vs DC 20
   - Result: Success
   - Effect: Marketplace built

### Phase 6: Summary
- Hexes: 10
- Regular Unrest: 1
- Imprisoned Unrest: 1/1 (Stocks full)

---

## Turn 7 - Party Level 5 (DC 20)

### Phase 1: Gain Fame
- Total: 8

### Phase 2: Apply Modifiers
- Passive Unrest: +1 (10 hexes)
- Starting: 1
- New: 2

### Phase 3: Kingdom Event
- DC: 11
- Roll: 19
- Event: **Disease Outbreak**
- Must be resolved or +1 Unrest/turn

### Phase 4: Resources
- Food: +4
- Consumption: -2
- Net: +2

### Phase 5: Kingdom Actions
1. PC1 (Expert +12): Resolve Disease Event (Medicine)
   - Roll: 5+12 = 17 vs DC 20
   - Result: Failure
   - Effect: Disease continues

2. PC2 (Expert +12): Execute Prisoners
   - Roll: 18+12 = 30 vs DC 20
   - Result: Critical Success!
   - Effect: All imprisoned unrest removed, -1 regular unrest
   - Unrest: 1 (2-1)

3. PC3 (Trained +9): Deal with Disease (second attempt)
   - Roll: 14+9 = 23 vs DC 20
   - Result: Success
   - Effect: Disease resolved

4. PC4 (Trained +9): Upgrade Settlement
   - Roll: 11+9 = 20 vs DC 20
   - Result: Success
   - Effect: Town Level 2 → Level 3

5. Companions (+7): Deal with Unrest
   - Roll: 10+7 = 17 vs DC 20
   - Result: Failure
   - Effect: -1 Unrest
   - Unrest: 0

### Phase 6: Summary
- Hexes: 10
- Settlement: Town Level 3
- Unrest: 0 (barely managed)

---

## Turn 8 - Party Level 6 (DC 22)

### Phase 1: Gain Fame
- Total: 9

### Phase 2: Apply Modifiers
- Passive Unrest: +1 (10 hexes)
- Starting: 0
- New: 1

### Phase 3: Kingdom Event
- DC: 16
- Roll: 8
- Event: None

### Phase 4: Resources
- Food: +4
- Consumption: -2
- Net: +2

### Phase 5: Kingdom Actions
1. PC1 (Expert +13): Claim Hex
   - Roll: 15+13 = 28 vs DC 22
   - Result: Success
   - Effect: 1 hex claimed (11 total)

2. PC2 (Expert +13): Build Structure (Jail - T2 Justice)
   - Roll: 10+13 = 23 vs DC 22
   - Result: Success
   - Effect: Jail built (holds 2 imprisoned unrest)

3. PC3 (Trained +10): Recruit Army
   - Roll: 17+10 = 27 vs DC 22
   - Result: Success
   - Effect: First army recruited

4. PC4 (Trained +10): Deal with Unrest
   - Roll: 8+10 = 18 vs DC 22
   - Result: Failure
   - Effect: -1 Unrest
   - Unrest: 0

5. Companions (+8): Claim Hex
   - Roll: 12+8 = 20 vs DC 22
   - Result: Failure
   - Effect: No hex

### Phase 6: Summary
- Hexes: 11
- Armies: 1
- Unrest: 0 (constant pressure)

---

## Turn 9 - Party Level 6 (DC 22)

### Phase 1: Gain Fame
- Total: 10 (max)

### Phase 2: Apply Modifiers
- Passive Unrest: +1 (11 hexes)
- Starting: 0
- New: 1

### Phase 3: Kingdom Event
- DC: 11
- Roll: 16
- Event: **Trade Opportunity** (+5 Gold)

### Phase 4: Resources
- Food: +4
- Consumption: -3 (Town + Army)
- Net: +1
- Gold: 10

### Phase 5: Kingdom Actions
1. PC1 (Expert +13): Build Structure (Amphitheater - T2 Culture)
   - Roll: 18+13 = 31 vs DC 22
   - Result: Success
   - Effect: Amphitheater built (+2 to unrest checks)

2. PC2 (Expert +13): Claim Hex
   - Roll: 11+13 = 24 vs DC 22
   - Result: Success
   - Effect: 1 hex claimed (12 total)

3. PC3 (Trained +10): Arrest Dissidents
   - Roll: 20+10 = 30 vs DC 22
   - Result: Success
   - Effect: Convert 2 Unrest → imprisoned (but only 1 regular)
   - Imprisoned: 1/2

4. PC4 (Trained +10): Claim Hex
   - Roll: 6+10 = 16 vs DC 22
   - Result: Failure
   - Effect: No hex

5. Companions (+8): Create Worksite
   - Roll: 14+8 = 22 vs DC 22
   - Result: Success
   - Effect: New worksite created

### Phase 6: Summary
- Hexes: 12
- Regular Unrest: 0
- Imprisoned: 1/2
- Better unrest management tools

---

## Turn 10 - Party Level 6 (DC 22)

### Phase 1: Gain Fame
- Total: 10

### Phase 2: Apply Modifiers
- Passive Unrest: +1 (12 hexes)
- Starting: 0
- New: 1

### Phase 3: Kingdom Event
- DC: 16
- Roll: 2
- Event: None

### Phase 4: Resources
- Food: +6
- Consumption: -3
- Net: +3

### Phase 5: Kingdom Actions
1. PC1 (Expert +13): Upgrade Settlement
   - Roll: 14+13 = 27 vs DC 22
   - Result: Success
   - Effect: Town Level 3 → Level 4

2. PC2 (Expert +13): Claim Hex
   - Roll: 8+13 = 21 vs DC 22
   - Result: Failure
   - Effect: No hex

3. PC3 (Trained +10): Deal with Unrest (+2 from Amphitheater)
   - Roll: 15+10+2 = 27 vs DC 22
   - Result: Success
   - Effect: -2 Unrest
   - Unrest: 0

4. PC4 (Trained +10): Recruit Army
   - Roll: 11+10 = 21 vs DC 22
   - Result: Failure
   - Effect: No army

5. Companions (+8): Build Structure
   - Roll: 13+8 = 21 vs DC 22
   - Result: Failure
   - Effect: No structure

### Phase 6: Summary
**Turn 10 Checkpoint:**
- Hexes: 12 (Target 6-8, exceeded)
- Settlement: Town Level 4 (Target 2+, exceeded)
- Worksites: 5 (Target 3-4, exceeded)
- Structures: 5 (Target 2-3, exceeded)
- Armies: 1 (Target 0-1, met)
- Unrest: 0 (but constant +1/turn pressure)
- Imprisoned: 1/2

---

## Turns 11-20 Summary (Party Levels 6-8)

### Turn 11 (Level 7, DC 23)
- Master proficiency unlocked! PC1 & PC2 at +15
- Passive Unrest: +1 (12 hexes)
- PC1 claims 2 hexes (Master ability)
- Unrest management ongoing

### Turn 12
- Hexes: 14
- Event: Border tensions
- Passive Unrest still +1
- PC3 arrests dissidents (imprisoned: 2/2)

### Turn 13
- Town upgraded to Level 5 (City!)
- Hexes: 15
- Passive pressure increasing

### Turn 14
- **Hexes: 16 - NEW THRESHOLD!**
- **Passive Unrest: +2/turn now**
- Emergency unrest management
- Execute prisoners to make room

### Turn 15
- PC4 critical failure on recruitment (+1 Unrest)
- Unrest spiking to 4
- Crisis mode activated

### Turn 16
- Build Prison (T3 Justice, holds 4)
- Mass arrests (4 imprisoned)
- Regular unrest reduced

### Turn 17
- City upgraded to Level 6
- Hexes: 18
- Passive: +2/turn continues

### Turn 18
- Event: Monster attack
- Successfully defended
- Unrest management critical

### Turn 19
- Multiple Deal with Unrest actions
- Barely maintaining stability

### Turn 20 (Level 8, DC 24)
**Turn 20 Checkpoint:**
- Hexes: 19 (Target 10-14, exceeded)
- Settlement: City Level 6 (Target Town 3-4, far exceeded)
- Passive Unrest: +2/turn
- Regular Unrest: 2
- Imprisoned: 3/4
- Average Unrest so far: 2.1

---

## Turns 21-30 Summary (Party Levels 8-10)

### Turn 21
- Continued expansion
- 20 hexes controlled
- Passive: +2/turn

### Turn 22
- Build Playhouse (T3 Culture)
- +2 to unrest checks but no automatic reduction
- Still struggling with +2/turn

### Turn 23
- Event: Plague returns
- Crisis management
- Unrest: 5 (penalty threshold!)

### Turn 24
- **Hexes: 24 - NEW THRESHOLD!**
- **Passive Unrest: +3/turn now**
- All actions at -1 penalty

### Turn 25
- Emergency measures
- Festival action (costs 5 Gold, -2 Unrest)
- Multiple arrests

### Turn 26
- City Level 7 achieved
- Unrest: 6
- Serious crisis

### Turn 27 (Level 9, DC 26)
- PC1 & PC2 at +17
- Focus entirely on stability
- Execute all prisoners

### Turn 28
- Unrest reduced to 3
- Breathing room achieved
- Halt expansion

### Turn 29
- Maintain status quo
- No new hexes claimed
- Focus on infrastructure

### Turn 30 (Level 10, DC 27)
**Turn 30 Checkpoint:**
- Hexes: 24 (Target 15-20, exceeded)
- Settlement: City Level 7 (Target City 5+, achieved)
- Passive Unrest: +3/turn
- Regular Unrest: 4
- Imprisoned: 2/4
- Average Unrest: 3.8

---

## Turns 31-40 Summary (Party Levels 10-12)

### Turn 31
- Decision: Stop expanding
- Focus on reaching Metropolis
- Build towards Auditorium

### Turn 32
- **City Level 8 - METROPOLIS!**
- **Passive Unrest: +3 (hexes) +1 (Metropolis) = +4/turn!**
- Crisis immediately

### Turn 33
- Unrest: 8
- -1 penalty to all actions
- Emergency management

### Turn 34
- Cannot build Auditorium yet (need resources)
- Mass arrests
- Prison full (4/4)

### Turn 35 (Level 11, DC 28)
- PC1 & PC2 at +19
- Build second Prison
- Total capacity: 8 imprisoned

### Turn 36
- Finally build Auditorium!
- -1/turn automatic (net +3/turn now)
- Some relief

### Turn 37
- Unrest stabilizing at 5
- Constant management required
- No expansion

### Turn 38
- Event: Invasion threat
- Successfully defended
- Unrest spike from war

### Turn 39
- Recovery phase
- Focus on stability
- Unrest: 6

### Turn 40 (Level 12, DC 30)
**Turn 40 Checkpoint:**
- Hexes: 24 (Target 20-25, met)
- Settlement: Metropolis Level 8 (Target City 6-7, exceeded)
- Passive Unrest: +3/turn (net after Auditorium)
- Regular Unrest: 5
- Imprisoned: 6/8
- Average Unrest: 4.5

---

## Turns 41-50 Final Phase (Party Levels 12-15)

### Turn 41
- Metropolis Level 9
- Still +3 net unrest/turn
- Constant crisis

### Turn 42
- Build Donjon (T4 Justice)
- 8 imprisoned capacity
- Auto-convert 1/turn

### Turn 43 (Level 13, DC 31)
- PC1 & PC2 at +21
- Somewhat stable
- Unrest: 4

### Turn 44
- Event: Golden Age attempt
- Requires Unrest < 3
- Cannot achieve!

### Turn 45
- All efforts on stability
- Multiple Deal with Unrest
- Festival held

### Turn 46
- PC4 critical failure (+1 Unrest)
- Back to crisis
- Unrest: 6

### Turn 47 (Level 14, DC 32)
- Execute all prisoners
- Dramatic reduction
- Unrest: 2

### Turn 48
- Brief respite
- Build monuments
- Passive still +3/turn

### Turn 49
- Final push
- Mass arrests
- Preparing for end

### Turn 50 (Level 15, DC 34)
- PC1 & PC2 Legendary (+24)
- Final Deal with Unrest
- End with Unrest: 3

---

## Final Statistics (Turn 50)

**Settlement:**
- 1 Metropolis (Level 9)
- 18 Structures built
- Auditorium, Donjon, 2 Prisons

**Territory:**
- 24 hexes controlled (expansion halted)
- 15 worksites active
- Limited by unrest pressure

**Resources:**
- Food: 38/48 stored
- Gold: 67 (many festivals)
- Materials: Moderate

**Military:**
- 2 armies maintained
- Minimal military due to focus on stability

**Kingdom Status:**
- Regular Unrest: 3
- Imprisoned Unrest: 7/8
- Fame: 10
- **Average Unrest: 4.2** (compared to 0.8 in Sim #005)

---

## Success Evaluation

### Minimum Success ✓
- [x] Town achieved (Turn 4)
- [x] 15+ hexes controlled
- [x] Unrest never exceeded 10 (peaked at 8)
- [x] No settlement lost
- [x] Positive gold balance

### Standard Success ✓
- [x] City achieved (Turn 13)
- [x] 20-25 hexes controlled (24)
- [ ] Average unrest below 5 (4.2 - close!)
- [x] Won at least 1 conflict
- [x] 50+ gold accumulated

### Exceptional Success ✗
- [x] Metropolis achieved (Turn 32)
- [ ] 30+ hexes controlled (stopped at 24)
- [ ] Average unrest below 3 (4.2)
- [x] Multiple victories
- [ ] 100+ gold accumulated (only 67)

**Final Rating: STANDARD SUCCESS** (barely)

---

## Analysis & Insights

### Unrest Was THE Central Challenge

**Unrest Management Actions (50 turns):**
- Deal with Unrest: 23 times
- Arrest Dissidents: 12 times
- Execute Prisoners: 8 times
- Festivals: 6 times (30 Gold spent)
- **Total: 49 unrest-related actions** (vs 3 in Sim #005)

### Key Pressure Points

1. **Turn 8-10:** First passive unrest (8+ hexes)
2. **Turn 14:** Jump to +2/turn (16+ hexes)
3. **Turn 24:** Jump to +3/turn (24+ hexes)
4. **Turn 32:** Metropolis adds +1 more (+4 total!)
5. **Turn 36:** Auditorium provides only partial relief

### Strategic Adaptations

1. **Expansion Halted:** Stopped at 24 hexes to avoid +4 passive
2. **Justice Infrastructure:** Built 2 Prisons + Donjon
3. **Culture Buildings:** Essential for check bonuses
4. **Military Minimized:** Only 2 armies to focus on stability
5. **Imprisonment Vital:** Constantly full prisons

### What Worked

- Early justice infrastructure (Stocks Turn 5)
- Amphitheater for +2 to checks
- Stopping expansion at 24 hexes
- Auditorium as soon as possible
- Using imprisonment to "bank" unrest

### What Didn't Work

- Trying to maintain normal growth
- Expanding past 24 hexes
- Building military
- Pursuing other objectives

### System Balance Assessment

The hex-based unrest system (+1 per 8 hexes + Metropolis) successfully:
- Made unrest management central to gameplay
- Created meaningful expansion decisions
- Made imprisonment mechanics essential
- Forced strategic trade-offs
- Prevented "runaway" success

However, it may be slightly overtuned:
- Metropolis becomes almost unviable (+4/turn is brutal)
- Action economy dominated by unrest (49/250 actions = 20%)
- Little room for other strategic choices
- Golden Age achievement impossible

---

## Conclusion

Simulation #006 with hex-based unrest (+1 per 8 hexes) and Metropolis penalty (+1) creates intense, constant pressure that makes unrest management the dominant challenge. The kingdom succeeded but was forced to halt expansion and focus almost entirely on stability.

The average unrest of 4.2 (vs 0.8 in #005) shows the system works as intended - unrest is now meaningful and imprisonment is essential. However, the Metropolis penalty combined with 24+ hex penalty (+4 total) may be excessive, creating a soft cap on kingdom growth.

**Recommendation:** The system works but could use minor tuning. Perhaps +1 per 10 hexes, or remove the Metropolis penalty, to allow for more strategic variety while keeping unrest relevant.
