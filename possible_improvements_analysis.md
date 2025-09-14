# Kingdom System - Possible Improvements Analysis

## Current Issues Identified from Simulation #001

### 1. Limited Hex Expansion (24/30 target)
**Problem:** Despite strong early growth, hex expansion plateaued
**Root Causes:**
- High DCs at later levels (DC 34 at Level 15)
- Action economy constraints
- No bonus for claiming multiple hexes efficiently

### 2. Single Settlement Focus
**Problem:** Only developed one primary settlement
**Root Causes:**
- High action cost to establish new settlements
- Resource drain from multiple settlements
- No clear mechanical incentive for multiple settlements

### 3. Late Game Stagnation
**Problem:** Growth plateaus after Level 12
**Root Causes:**
- DC scaling becomes prohibitive
- Diminishing returns on improvements
- Limited high-tier options

---

## Proposed Adjustments

### A. Hex Expansion Improvements

#### 1. **Claim Hex Scaling**
Current: Always claims 1 hex (2 on critical success)
Proposed: Scale with proficiency level
- Expert: 1 hex (2 on crit)
- Master: 2 hexes (3 on crit)
- Legendary: 3 hexes (4 on crit)

#### 2. **Adjacent Hex Bonus**
Add a +2 circumstance bonus when claiming hexes adjacent to 3+ controlled hexes

#### 3. **Explorer Structure**
New building that provides +2 to Claim Hex actions and allows claiming non-adjacent hexes

### B. Multiple Settlement Incentives

#### 1. **Settlement Network Bonuses**
- 2 settlements: +1 to all kingdom actions
- 3 settlements: +2 to all kingdom actions, +1 Fame/turn
- 4+ settlements: +3 to all kingdom actions, +2 Fame/turn

#### 2. **Specialized Settlements**
Allow settlements to specialize:
- Military Outpost: Reduced army costs, +2 to warfare
- Trade Hub: +Gold production, +2 to economy
- Agricultural Center: +Food production, +2 to industry
- Cultural Center: -Unrest, +2 to stability

#### 3. **Lower Secondary Settlement Costs**
- First settlement: Normal costs
- Second settlement: -2 DC to establish
- Third+ settlements: -4 DC to establish

### C. Late Game Progression Fixes

#### 1. **DC Scaling Adjustment**
Current progression:
- Level 12: DC 30
- Level 13: DC 31
- Level 14: DC 32
- Level 15: DC 34

Proposed progression:
- Level 12: DC 30
- Level 13: DC 30 (no increase)
- Level 14: DC 31
- Level 15: DC 32

#### 2. **High-Tier Structure Bonuses**
Structures built at City+ level provide cumulative bonuses:
- Each T3 structure: +1 to related actions
- Each T4 structure: +2 to related actions
- Maximum +10 from structures

#### 3. **Metropolis Benefits**
Reaching Metropolis provides:
- +4 to all kingdom actions (instead of +2)
- Can take 2 kingdom actions per PC per turn
- Automatic success on routine actions (DC 15 or lower)

### D. Alternative Strategic Paths

#### 1. **Wide Empire** (Multiple Small Settlements)
- Bonuses for 30+ hexes controlled
- Reduced unrest from distributed population
- Higher resource generation

#### 2. **Tall Empire** (Single Mega-City)
- Bonuses for settlement level 10+
- Powerful unique structures
- Cultural dominance effects

#### 3. **Trade Empire** (Connected Settlements)
- Bonuses for road networks
- Trade route multipliers
- Diplomatic advantages

---

## Specific Rule Modifications

### Modified Claim Hex Action
**Requirement:** Must be adjacent to controlled hex (unless you have Explorer's Guild)
**Effect:** 
- Expert/Trained: Claim 1 hex (2 on critical success)
- Master: Claim 2 hexes (3 on critical success)  
- Legendary: Claim 3 hexes (4 on critical success)
**Modifiers:**
- +2 if adjacent to 3+ controlled hexes
- +2 with Explorer's Guild
- Can spend Fame to claim additional hex (5 Fame per extra hex)

### New Settlement Action
**Establish Settlement**
**Requirement:** Controlled hex without settlement
**DC Modifier:** 
- Second settlement: -2
- Third settlement: -4
- Fourth+ settlement: -6
**Benefits:** Each settlement can specialize and provides network bonuses

### Settlement Development Tracks
Instead of linear progression, settlements can branch:

**Village (Level 0-1)**
↓
**Town (Level 2-4)**
↓ (Choose specialization)
- **Trade City** → Trade Metropolis (economy focus)
- **Fortress City** → Military Capital (warfare focus)
- **Garden City** → Agricultural Hub (industry focus)
- **Culture City** → Grand Capital (stability focus)

Each path provides different bonuses and structures.

---

## Expected Outcomes with Adjustments

### Turn 10 (Level 6)
- Hexes: 10-12 (vs 10 actual)
- Settlements: 1-2 (vs 1 actual)
- Primary: Town L3-4
- Secondary: Village L0-1

### Turn 20 (Level 8)
- Hexes: 18-22 (vs 21 actual)
- Settlements: 2-3 (vs 1 actual)
- Primary: City L5-6
- Secondary: Town L2-3

### Turn 30 (Level 10)
- Hexes: 25-30 (vs 24 actual)
- Settlements: 3-4 (vs 1 actual)
- Primary: City L7-8
- Secondaries: Towns/Villages

### Turn 50 (Level 15)
- Hexes: 35-40 (vs 24 actual)
- Settlements: 4-5 (vs 1 actual)
- Primary: Metropolis L9-10
- Network bonuses active

---

## Implementation Priority

### High Priority (Core Fixes)
1. Claim Hex scaling with proficiency
2. DC progression adjustment for Levels 13-15
3. Settlement network bonuses

### Medium Priority (Strategic Depth)
1. Settlement specialization options
2. Explorer structure for expansion
3. High-tier structure bonuses

### Low Priority (Polish)
1. Alternative empire paths
2. Fame-for-hexes exchange
3. Automatic success on routine actions

---

## Testing Recommendations

Run 3-5 new simulations with these adjustments to verify:
1. Hex count reaches 30+ by Turn 50
2. Multiple settlements are viable
3. Late game remains engaging
4. Different strategies can succeed
5. Critical moments still impactful

The goal is to maintain the ~65% success rate while enabling more ambitious kingdom growth and strategic variety.
