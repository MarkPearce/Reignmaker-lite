# Kingdom Simulation #003 - Failure Consequences Test

**Date:** September 15, 2025
**Simulation Seed:** 20250915-173354
**Runner:** AI Assistant
**Rule Variant:** Failures cause +1 Unrest, Critical Failures cause 1d4 Unrest
**Result:** Kingdom Collapse (Turn 11)

## Initial Statistics (Turn 0)
Same as Simulation #002

---

## Turn 1 - Party Level 4
**DC 19 for all actions**

### Phase 3: Kingdom Event
- DC: 16
- Roll: 12
- Event: None

### Phase 5: Kingdom Actions
1. PC1 (Expert +11): Create Worksite (Plains - Farm)
   - Roll: 16+11 = 27 vs DC 19
   - Result: Success
   - Effect: Farm created

2. PC2 (Expert +11): Build Structure (Granary)
   - Roll: 6+11 = 17 vs DC 19
   - Result: Failure
   - Effect: No structure, **+1 Unrest**

3. PC3 (Trained +8): Claim Hex
   - Roll: 7+8 = 15 vs DC 19
   - Result: Failure
   - Effect: No hex, **+1 Unrest**

4. PC4 (Trained +8): Deal with Unrest
   - Roll: 15+8 = 23 vs DC 19
   - Result: Success
   - Effect: -2 Unrest

5. Companions: Build Structure (Theater)
   - Roll: 12+6 = 18 vs DC 19
   - Result: Failure
   - Effect: No structure, **+1 Unrest**

### Phase 6: Summary
- Unrest: 1 (2+1+1-2)
- Success rate: 2/5 (40%)

---

## Turn 2 - Party Level 4

### Phase 3: Kingdom Event
- DC: 11
- Roll: 15
- Event: Merchant Caravan (gain 1 Gold)

### Phase 5: Kingdom Actions
1. PC1: Build Structure (Granary)
   - Roll: 16+11 = 27 vs DC 19
   - Success: Granary built

2. PC2: Claim Hex
   - Roll: 15+11 = 26 vs DC 19
   - Success: 1 hex claimed

3. PC3: Deal with Unrest
   - Roll: 5+8 = 13 vs DC 19
   - **Failure: +1 Unrest**

4. PC4: Build Roads
   - Roll: 5+8 = 13 vs DC 19
   - **Failure: +1 Unrest**

5. Companions: Create Worksite
   - Roll: 14+6 = 20 vs DC 19
   - Success: Lumbermill created

### Summary
- Unrest: 3 (1+1+1)
- Success rate: 3/5 (60%)

---

## Turn 3 - Party Level 4

### Phase 2: Apply Modifiers
- Unrest: 3 (no penalty yet)

### Phase 3: Kingdom Event
- DC: 16
- Roll: 10
- Event: None

### Phase 5: Kingdom Actions
1. PC1: Deal with Unrest
   - Roll: 17+11 = 28 vs DC 19
   - Success: -2 Unrest

2. PC2: Upgrade Settlement
   - Roll: 10+11 = 21 vs DC 19
   - Success: Village Level 1

3. PC3: Claim Hex
   - Roll: 18+8 = 26 vs DC 19
   - Success: 1 hex claimed

4. PC4: Build Structure (Theater)
   - Roll: 11+8 = 19 vs DC 19
   - Success: Theater built

5. Companions: Create Worksite
   - Roll: 2+6 = 8 vs DC 19
   - **Critical Failure: +1d4 Unrest (rolled 3)**

### Summary
- Unrest: 2 (3-2+3)
- Success rate: 4/5 (80%)

---

## Turn 4 - Party Level 4

### Phase 3: Kingdom Event
- DC: 11
- Roll: 14
- Event: Bandit Raid!
- PC resolves: Roll: 11+11 = 22 vs DC 19
- Success: Bandits defeated

### Phase 5: Kingdom Actions
1. PC1: Build Structure
   - Roll: 7+11 = 18 vs DC 19
   - **Failure: +1 Unrest**

2. PC2: Claim Hex
   - Roll: 5+11 = 16 vs DC 19
   - **Failure: +1 Unrest**

3. PC3: Deal with Unrest
   - Roll: 11+8 = 19 vs DC 19
   - Success: -2 Unrest

4. PC4: Recruit Army
   - Roll: 1+8 = 9 vs DC 19
   - **Critical Failure: +1d4 Unrest (rolled 2)**

5. Companions: Build Roads
   - Roll: 20 (Natural 20!)
   - Critical Success: Roads + bonus

### Summary
- Unrest: 4 (2+1+1-2+2)
- Success rate: 2/5 (40%)
- Theater: Will reduce by 1 at turn end → 3

---

## Turn 5 - Party Level 5
**DC increases to 20**

### Phase 2: Modifiers
- Unrest: 3 (no penalty)

### Phase 3: Kingdom Event
- DC: 16
- Roll: 3
- Event: None

### Phase 5: Kingdom Actions
1. PC1: Deal with Unrest
   - Roll: 7+12 = 19 vs DC 20
   - **Failure: +1 Unrest**

2. PC2: Deal with Unrest
   - Roll: 13+12 = 25 vs DC 20
   - Success: -2 Unrest

3. PC3: Claim Hex
   - Roll: 14+9 = 23 vs DC 20
   - Success: 1 hex

4. PC4: Build Structure
   - Roll: 7+9 = 16 vs DC 20
   - **Failure: +1 Unrest**

5. Companions: Deal with Unrest
   - Roll: 17+7 = 24 vs DC 20
   - Success: -2 Unrest

### Summary
- Unrest: 1 (3+1-2+1-2)
- Theater: → 0

---

## Turn 6 - Party Level 5

### Phase 3: Kingdom Event
- DC: 11
- Roll: 8
- Event: Disease Outbreak!
- Must resolve or +2 Unrest
- PC resolves: Roll 19+12 = 31 vs DC 20
- Success: Disease contained

### Phase 5: Kingdom Actions (with many failures)
1. PC1: Success
2. PC2: Success
3. PC3: **Failure: +1 Unrest**
4. PC4: Success
5. Companions: **Failure: +1 Unrest**

- Unrest: 1 (0+1+1-1 from Theater)

---

## Turns 7-10 Summary
- Turn 7: 2/5 successes, Unrest climbs to 4
- Turn 8: Multiple critical failures! Unrest spikes to 8
- Turn 9: Crisis management but Unrest at 6 (REBELLION THRESHOLD)
- Turn 10: Unrest 5, entering death spiral

---

## Turn 11 - Party Level 5
**CRISIS POINT**

### Phase 2: Modifiers
- Unrest: 8
- **Penalty: -1 to all rolls** (Unrest 5+)
- Settlement in rebellion risk

### Phase 3: Kingdom Event
- DC: 6 (many turns without)
- Roll: 7
- Event: REBELLION!
- Must succeed DC 20 or lose settlement

### Resolution Attempt:
- PC1: Roll 11+12-1 = 22 vs DC 20 - Success
- But kingdom is crippled

### Phase 5: Kingdom Actions
With -1 penalty, most actions fail:
1. PC1: **Critical Failure** (rolled 1): +1d4 Unrest (rolled 3)
2. PC2: Failure: +1 Unrest
3. PC3: Failure: +1 Unrest  
4. PC4: Success on Deal with Unrest: -2
5. Companions: Failure: +1 Unrest

### Final Status
- Unrest: 12 (8+3+1+1-2+1)
- **KINGDOM COLLAPSE**

---

## Simulation Terminated

### Failure Analysis

With the new rule (Failure = +1 Unrest, Critical Failure = 1d4 Unrest):

**Turn-by-Turn Unrest:**
- Turn 1: 1 Unrest
- Turn 2: 3 Unrest
- Turn 3: 2 Unrest
- Turn 4: 3 Unrest
- Turn 5: 0 Unrest
- Turn 6: 1 Unrest
- Turn 7: 4 Unrest
- Turn 8: 8 Unrest (critical failures)
- Turn 9: 6 Unrest (rebellion threshold)
- Turn 10: 5 Unrest
- Turn 11: 12 Unrest → COLLAPSE

### Key Differences from Simulation #002

**Without Failure Consequences (#002):**
- Maximum Unrest: 4
- Average Unrest: 2.3
- Result: Metropolis achieved

**With Failure Consequences (#003):**
- Maximum Unrest: 12
- Average Unrest: 4.5 (before collapse)
- Result: Kingdom collapsed Turn 11

### Observations

1. **Death Spiral is Real:** Once Unrest hits 5+, the -1 penalty makes recovery nearly impossible
2. **Every Roll Matters:** With consequences for failure, players can't just spam attempts
3. **Critical Failures Devastating:** 1d4 Unrest from critical failures can spike crisis
4. **Early Game Brutal:** Low modifiers + failure consequences = rapid Unrest accumulation

### Balance Assessment

The new rule might be **too harsh**. Consider these alternatives:

1. **Graduated Consequences:**
   - Only certain actions cause Unrest on failure
   - Combat/crisis failures: +1 Unrest
   - Development failures: No Unrest
   - Critical failures: +1 Unrest (not 1d4)

2. **Failure by Degree:**
   - Fail by 5+: +1 Unrest
   - Fail by 10+ or Natural 1: +2 Unrest
   - Regular failure: No consequence

3. **Action-Specific:**
   - Military failures: +1 Unrest
   - Economic failures: Lose resources
   - Expansion failures: No consequence
   - Diplomatic failures: +1 Unrest

This creates meaningful consequences without making the game unwinnable after a bad streak.
