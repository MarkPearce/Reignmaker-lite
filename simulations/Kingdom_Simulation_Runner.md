# Kingdom Simulation Runner for Reignmaker-lite

## Purpose
This document serves as a simulation runner for the Reignmaker-lite subsystem for Pathfinder 2e. Each time you run this simulation, it will:
1. Generate a unique 50-turn simulation with fresh dice rolls
2. Create a numbered output file (kingdom_simulation_001.md, _002.md, etc.)
3. Update the master analysis document with aggregated results

---

## 🎲 RUN NEW SIMULATION

**To run a new simulation:**

1. **Check existing simulations** to determine the next number:
   - Look for files named `kingdom_simulation_###.md`
   - Use the next sequential number

2. **Generate a unique random seed:**
   - Use current timestamp: `YYYYMMDD-HHMMSS`
   - Or create a random d20 sequence (100-200 rolls)
   - Document the seed/sequence at the start of your simulation

3. **Create simulation files:**
   - Main file: `kingdom_simulation_###.md` (detailed turn-by-turn log)
   - Summary file: `kingdom_simulation_###_summary.md` (readable highlights)
   - Follow the structure and rules below
   - Use actual d20 rolls (not flat averages)

4. **Update master analysis:**
   - Add results to `kingdom_system_analysis.md`
   - Compare to previous simulations
   - Note any patterns or anomalies

---

## Initial Kingdom Setup

### Starting Conditions (Turn 0)
**Every simulation starts with these exact parameters:**

**Settlement:**
- 1 Village (Level 0)
- Located in a Plains hex (central position recommended)
- No starting structures

**Territory:**
- 3 controlled hexes total
- Recommended configuration:
  - 1 Plains hex (settlement location)
  - 1 Forest hex (adjacent)
  - 1 Hills hex (adjacent)

**Worksites:**
- Plains: None initially
- Forest: None initially
- Hills: None initially

**Resources:**
- Food: 0
- Gold: 0
- Lumber/Stone/Ore: 0 (cannot be stored initially)

**Military:**
- 0 armies (none recruited)

**Kingdom Status:**
- Unrest: 0
- Fame: 1
- Not at war
- No diplomatic relationships yet

**Player Characters:**
- 4 PCs at Level 4 (starting level)
- Companions available for collective action
- 2 PCs with Expert proficiency (+11) in their primary skill
- 2 PCs with Trained proficiency (+8) in their primary skill

---

## Core Mechanics

### Unrest System (Updated)

#### Unrest Tiers and Penalties
The unrest system now uses a gentler penalty progression with specific incident triggers:

| Tier | Unrest Range | Penalty | Incidents |
|------|-------------|---------|-----------|
| **0: Stable** | 0-2 | None | No incidents |
| **1: Discontent** | 3-5 | -1 to all checks | Roll on Minor Incidents table |
| **2: Turmoil** | 6-8 | -2 to all checks | Roll on Moderate Incidents table |
| **3: Rebellion** | 9+ | -3 to all checks (capped) | Roll on Major Incidents table |

#### Passive Unrest Sources
**Territory Size:** The administrative burden of controlling territory generates unrest:
- **8-15 hexes:** +1 Unrest per turn
- **16-23 hexes:** +2 Unrest per turn
- **24-31 hexes:** +3 Unrest per turn
- **32+ hexes:** +4 Unrest per turn

**Metropolis Burden:** Each Metropolis generates **+1 additional Unrest per turn** due to urban complexity.

#### Active Unrest Sources
**Failed Actions (Selective):** Only certain critical actions cause unrest on failure:
- Crisis Response Actions: Resolve Kingdom Event, Deal with Unrest, Execute/Pardon Prisoners
- Military Operations: Recruit Army, Deploy Army, Disband Army
- Public Order: Arrest Dissidents
- Other development/economic actions: No unrest on failure

**Resource Shortages:**
- Food shortage: +1 Unrest per missing Food each turn
- Unsupported armies: +1 Unrest per excess army each turn

**Other Sources:**
- Being at war: +1 Unrest per turn
- Failed army morale checks: +1 Unrest (or +2 on critical failure)
- Army disbanding: +1 Unrest (or +2 if through mutiny/desertion)
- Unresolved kingdom events: Variable

#### Incident Resolution
**When:** At the start of each Kingdom Turn (Phase 2), after calculating current unrest tier

**Process:**
1. Determine unrest tier (0-3)
2. If tier 1+, roll d100 on appropriate incident table
3. Resolve incident with skill check (does NOT consume a Kingdom Action)
4. Apply immediate consequences

**Incident Tables:** See Unrest_incidents.md for complete tables

### Critical Implementation Requirements

#### 1. Kingdom Level = Party Level
The kingdom level advances in lockstep with party level. This represents the PCs' growing expertise as leaders and the kingdom's increasing sophistication.

#### 2. All Actions Use Level-Based DCs
**Every kingdom action uses the Level-based DC:**
- Level 4: DC 19
- Level 5: DC 20
- Level 6: DC 22
- Level 7: DC 23
- Level 8: DC 24
- Level 9: DC 26
- Level 10: DC 27
- Level 11: DC 28
- Level 12: DC 30
- Level 13: DC 31
- Level 14: DC 32
- Level 15: DC 34

**No fixed DCs exist** - everything scales with kingdom/party level.

#### 3. Skill Proficiency Distribution
- 2 PCs always have the highest available proficiency
- 2 PCs always have the second-highest available proficiency
- Proficiency unlocks: Expert (L3), Master (L7), Legendary (L15)

#### 4. Actual d20 Rolls Required
Using flat averages or success percentages alone misses critical successes and failures, which are essential for:
- Narrative drama
- Risk/reward decisions
- Fame generation (critical successes grant Fame)
- Unrest consequences (critical failures may add Unrest)

### Dice Resolution (Pathfinder 2e Rules)
**Use actual d20 rolls for each check:**
- Roll: 1d20 + modifier vs DC
- **Critical Success:** Total beats DC by 10 or more
- **Critical Failure:** Total fails DC by 10 or more  
- **Success:** Total meets or exceeds DC (without critical)
- **Failure:** Total below DC (without critical)

**IMPORTANT:** Natural 20s and 1s do NOT automatically create critical results in Pathfinder 2e. Only the degree of success matters (beating/failing by 10+).

### PC Skill Progression
**Proficiency levels by party level:**
- **Levels 3-6:** 2 PCs have Expert, 2 PCs have Trained
- **Levels 7-14:** 2 PCs have Master, 2 PCs have Expert
- **Levels 15+:** 2 PCs have Legendary, 2 PCs have Master

**Modifiers (assuming +4 ability):**
- Trained: Level + 6
- Expert: Level + 8
- Master: Level + 10
- Legendary: Level + 12

---

## Turn Structure

Each turn follows these 6 phases:

### Phase 1: Gain Fame
- Gain 1 Fame automatically at start of turn
- Critical successes on kingdom actions grant additional Fame
- Note available Fame for rerolls

### Phase 2: Apply Modifiers & Check for Incidents
- Check if at war (+1 Unrest if yes)
- Calculate passive unrest from territory/metropolises
- Determine current unrest tier (0-3)
- **If Tier 1+:** Roll d100 on appropriate incident table and resolve immediately
- Apply structure bonuses
- Calculate Unrest penalty based on tier (-0 to -3)

### Phase 3: Kingdom Event Check
- Start at DC 16
- Reduce by 5 each turn without event (min DC 6)
- Reset to DC 16 after event occurs
- Roll d20 vs DC

### Phase 4: Resource Management
- Calculate production from all worksites
- Subtract consumption (settlements + armies)
- Check for food shortages (generate unrest if any)
- Apply storage limits
- Process construction projects
- Resources not used/traded are lost at end of turn

### Phase 5: Kingdom Actions
- Each PC takes one action
- Companions take one collective action
- Apply all modifiers including unrest penalty
- Roll d20 for each action
- Critical successes grant +1 Fame
- Some critical failures cause +1 Unrest (see selective list)
- Record actual roll, modifier, total, and result type

### Phase 6: End of Turn
- Update all kingdom statistics
- Lose unused Lumber/Stone/Ore (no storage)
- Check for milestone achievements
- Note any special conditions

---

## Turn Tracking Template

```markdown
## Turn [X] - Party Level [Y]
**Simulation Seed:** [Your unique seed/timestamp]

### Phase 1: Gain Fame
- Starting Fame: [X]
- Gained: +1 (automatic)
- Total: [X]

### Phase 2: Apply Modifiers & Incidents
- At War: [Yes/No] (+1 Unrest if yes)
- Territory Unrest: +[X] ([# hexes])
- Metropolis Unrest: +[X] ([# metropolises])
- Current Unrest: [X] (Tier [0-3]: [Name])
- Unrest Penalty: -[0 to 3] to all checks
- **Incident Check:** [If tier 1+]
  - Roll d100: [Result]
  - Incident: [Name or "No Incident"]
  - Resolution: [Skill used, DC, roll, result]
  - Effect: [Consequences]
- Structure Bonuses: [List]

### Phase 3: Kingdom Event
- DC: [Current DC]
- Roll: [d20 result]
- Event: [None/Event Type]
- Resolution: [If event occurred]

### Phase 4: Resources
**Production:**
- Food: +[X] ([sources])
- Lumber: +[X] ([sources])
- Stone: +[X] ([sources])
- Ore: +[X] ([sources])

**Consumption:**
- Settlements: -[X] Food
- Armies: -[X] Food
- Net Food: [+/- amount]
- Food Shortage: [If any, causes +X Unrest]

**Storage:**
- Food Stored: [X]/[Max]
- Gold: [X]
- Resources Lost: [List of unused Lumber/Stone/Ore]

### Phase 5: Kingdom Actions
1. PC1 (Expert +11): [Action]
   - Modifiers: +11 skill -[unrest penalty] = +[total]
   - Roll: [d20]+[total] = [Result] vs DC [X]
   - Result: [Critical Failure/Failure/Success/Critical Success]
   - Effect: [What happened, +1 Fame if crit success, +1 Unrest if applicable crit fail]

2. PC2 (Expert +11): [Action]
   - Modifiers: +11 skill -[unrest penalty] = +[total]
   - Roll: [d20]+[total] = [Result] vs DC [X]
   - Result: [Type]
   - Effect: [What happened]

3. PC3 (Trained +8): [Action]
   - Modifiers: +8 skill -[unrest penalty] = +[total]
   - Roll: [d20]+[total] = [Result] vs DC [X]
   - Result: [Type]
   - Effect: [What happened]

4. PC4 (Trained +8): [Action]
   - Modifiers: +8 skill -[unrest penalty] = +[total]
   - Roll: [d20]+[total] = [Result] vs DC [X]
   - Result: [Type]
   - Effect: [What happened]

5. Companions: [Action]
   - Modifiers: +[base] -[unrest penalty] = +[total]
   - Roll: [d20]+[total] = [Result] vs DC [X]
   - Result: [Type]
   - Effect: [What happened]

### Phase 6: Summary
- Hexes: [X]
- Settlement: [Type and Level]
- Armies: [X]
- Unrest: [Final] (Tier [X])
- Fame: [X]
- Key Achievement: [If any]
```

---

## Milestone Checkpoints

Track these to ensure balanced progression:

### Turn 10 (Level 6)
Expected Status:
- Town (Level 2+)
- 6-8 hexes controlled
- 3-4 worksites active
- 2-3 structures built
- 0-1 armies
- Unrest: 0-3 (manageable)

### Turn 20 (Level 8)
Expected Status:
- Town Level 3-4
- 10-14 hexes controlled
- 5-6 worksites active
- 4-5 structures built
- 1-2 armies
- Unrest: 2-5 (some incidents)

### Turn 30 (Level 10)
Expected Status:
- City (Level 5+)
- 15-20 hexes controlled
- 7-9 worksites active
- 6-7 structures built
- 2-3 armies
- Unrest: 3-6 (regular management needed)

### Turn 40 (Level 12)
Expected Status:
- City Level 6-7
- 20-25 hexes controlled
- 10-12 worksites active
- 8-9 structures built
- 3-4 armies
- Unrest: 4-7 (active mitigation required)

### Turn 50 (Level 15)
Expected Status:
- Metropolis (Level 8+)
- 25-30 hexes controlled
- 13-15 worksites active
- 10-12 structures built
- 4-5 armies
- Unrest: 5-8 (constant attention needed)

---

## Success Metrics

Evaluate each simulation against these targets:

### Minimum Success
- [ ] Town achieved (Level 2+)
- [ ] 15+ hexes controlled
- [ ] Unrest never exceeded Tier 3 (9+)
- [ ] No settlement lost
- [ ] Positive gold balance

### Standard Success
- [ ] City achieved (Level 5+)
- [ ] 20-25 hexes controlled
- [ ] Average unrest below Tier 2 (6)
- [ ] Successfully resolved 5+ incidents
- [ ] 50+ gold accumulated

### Exceptional Success
- [ ] Metropolis achieved (Level 8+)
- [ ] 30+ hexes controlled
- [ ] Average unrest below Tier 1 (3)
- [ ] No major incidents triggered
- [ ] 100+ gold accumulated

---

## Unrest Incident Quick Reference

### Minor Incidents (Tier 1: Unrest 3-5)
Roll d100, 20% chance of no incident:
- Crime Wave, Work Stoppage, Emigration Threat
- Protests, Corruption Scandal, Rising Tensions
- Bandit Activity, Minor Diplomatic Incident

### Moderate Incidents (Tier 2: Unrest 6-8)
Roll d100, 15% chance of no incident:
- Production Strike, Tax Revolt, Infrastructure Damage
- Disease Outbreak, Riot, Settlement Crisis
- Assassination Attempt, Trade Embargo, Mass Exodus

### Major Incidents (Tier 3: Unrest 9+)
Roll d100, 10% chance of no incident:
- Guerrilla Movement, Mass Desertion Threat, International Scandal
- Prison Breaks, Noble Conspiracy, Economic Crash
- Religious Schism, Border Raid, Secession Crisis

---

## Event Guidelines

Roll d20 for random events or use this sequence for comparable simulations:

### Standard Event Schedule
- **Turn 3:** Bandit Activity
- **Turn 7:** Harvest Event
- **Turn 11:** Disease/Plague
- **Turn 16:** Trade Opportunity
- **Turn 21:** Border Conflict
- **Turn 26:** Discovery
- **Turn 32:** Cultural Event
- **Turn 38:** Monster/Threat
- **Turn 44:** Economic Event
- **Turn 49-50:** Final Challenge

### Random Event Types (d12)
1-2: Military threat
3-4: Economic opportunity
5-6: Natural disaster
7-8: Political intrigue
9-10: Resource discovery
11-12: Social/Cultural event

---

## Critical Success/Failure Guidelines

### Critical Success Effects
- **Development:** Jump 2 levels instead of 1
- **Resources:** Double production or finds
- **Military:** Elite unit or major victory
- **Diplomacy:** Alliance or major trade deal
- **Crisis:** Complete resolution + bonus
- **Always:** +1 Fame gained

### Critical Failure Effects
- **Development:** No progress + possible damage
- **Resources:** Loss or accident
- **Military:** Desertion or defeat (+1 Unrest for military actions)
- **Diplomacy:** War or embargo
- **Crisis:** Escalation + new problem (+1 Unrest for crisis actions)
- **Selective:** Only certain actions cause +1 Unrest on crit fail

---

## Action Priority Guidelines

When deciding PC actions each turn:

### Crisis Priority (Unrest Tier 2+)
1. Deal with Unrest (always available)
2. Arrest Dissidents (convert to imprisoned unrest)
3. Build unrest-reducing structures
4. Address incident root causes

### Growth Priority (Stable)
1. Develop settlements
2. Claim strategic hexes
3. Build key structures
4. Establish worksites

### Military Priority (Threatened)
1. Recruit armies
2. Build defenses
3. Train troops
4. Seek alliances

---

## Diplomatic Relations Tracking

### Attitude Levels
- **Helpful:** Military aid, favorable trade (-1 Gold on purchases), allows passage
- **Friendly:** Open to trade/alliances, -1 DC to diplomatic checks
- **Indifferent:** Standard rates, neutral in conflicts
- **Unfriendly:** Trade restrictions (+1 Gold tax), +2 DC to checks
- **Hostile:** No trade, may attack, +4 DC to checks, +1 Unrest per turn

### Diplomatic Capacity
Without diplomatic structures, cannot maintain Helpful relationships.
- Embassy (T2): +1 Helpful capacity
- Grand Embassy (T3): +2 Helpful capacity
- Diplomatic Quarter (T4): +3 Helpful capacity

---

## Simulation Output Format

### Main Simulation File (`kingdom_simulation_###.md`)
Should include:
- Header with date, seed, runner, result
- Initial statistics summary
- Detailed turn-by-turn logs (all 50 turns)
- Each turn showing rolls, decisions, and outcomes
- All incident resolutions
- Final statistics and analysis

### Summary File (`kingdom_simulation_###_summary.md`)
Should include a concise, readable summary with:

```markdown
# Kingdom Simulation #[Number] - Summary

**Date:** [When run]
**Result:** [Success level]

## Quick Stats
- Final Settlement: [Level and type]
- Territory: [X hexes]
- Gold: [Final amount]
- Armies: [Final count]
- Final Unrest: [X] (Tier [Y])

## Growth Trajectory
[Brief timeline showing major phases]

## Unrest Management
- Maximum Unrest: [Peak value and tier]
- Incidents Faced: [Total number and severity]
- Crisis Points: [When tier changes occurred]
- Average Unrest: [Overall average]

## Critical Moments
### Game-Changing Successes
[2-4 most impactful critical successes with Fame gains]

### Major Setbacks
[2-3 significant failures or incidents]

## Key Turning Points
[3-5 moments that defined the simulation]

## Strategic Insights
- What Worked: [Key successful strategies]
- Challenges: [Main difficulties faced]
- Sweet Spot: [Optimal configuration discovered]

## Final Assessment
[Brief narrative of overall progression and whether success criteria were met]
```

---

## Post-Simulation Checklist

After completing your simulation:

1. **Save simulation files:**
   - Main file: `kingdom_simulation_###.md` (detailed turns)
   - Summary: `kingdom_simulation_###_summary.md` (highlights)

2. **Update master analysis** in `kingdom_system_analysis_master.md`:
   - Add summary statistics
   - Compare to previous runs
   - Note any patterns
   - Update averages

3. **Document insights:**
   - What worked well?
   - What struggled?
   - Any rule clarifications needed?
   - Balance observations?

4. **File your results:**
   - Ensure proper numbering
   - Update index if one exists
   - Commit to version control

---

## Quick Reference Tables

### Settlement Progression
| Level | Settlement Type | Food/Turn | Max Structures | Army Support |
|-------|----------------|-----------|----------------|--------------|
| 0-1 | Village | 1 | 2 | 1 |
| 2-4 | Town | 4 | 4 | 2 |
| 5-7 | City | 8 | 8 | 3 |
| 8+ | Metropolis | 12 | Unlimited | 4 |

**Advancement Requirements:**
- Must have maximum structures for current tier before advancing
- Example: Village needs 2 structures to become Town at level 2

### Structure Tiers & Prerequisites
- T1: Village structures (available immediately)
- T2: Town structures (requires Town)
- T3: City structures (requires City)
- T4: Metropolis structures (requires Metropolis)

### Resource Management
| Resource | Storage Without Structures | Notes |
|----------|---------------------------|--------|
| Food | 0 | Only stockpiled resource |
| Gold | Unlimited | Flexible currency |
| Lumber/Stone/Ore | 0 | Lost if unused each turn |

**Trade Rates (Base):**
- Purchase: 2 Gold → 1 Resource
- Sell: 2 Resources → 1 Gold
- Commerce structures improve these rates

### Army Costs & Support
- Recruit: 1 Kingdom Action
- Maintain: 1 Food/turn per army
- Unsupported armies must make morale checks
- Failed morale: +1 Unrest (or +2 on crit fail)

---

## Troubleshooting

### Common Implementation Errors to Avoid

#### 1. Wrong Unrest System
❌ **Wrong:** "-1 per 5 unrest" or "escalating -2, -4, -6"
✅ **Correct:** Tier-based: 0-2 = no penalty, 3-5 = -1, 6-8 = -2, 9+ = -3

#### 2. Forgetting Incidents
❌ **Wrong:** Only tracking unrest penalties
✅ **Correct:** Roll on incident tables when tier 1+ each turn

#### 3. All Actions Cause Unrest on Failure
❌ **Wrong:** Every critical failure adds unrest
✅ **Correct:** Only crisis/military/public order actions

#### 4. Using Fixed DCs
❌ **Wrong:** "Claim Hex is always DC 14"
✅ **Correct:** Use Level-based DC from table

### Common Issues & Solutions

**Unrest Spiral:**
- Deal with Unrest action available every turn
- Arrest Dissidents to convert to imprisoned unrest
- Build Theater (T3): -1 Unrest per turn
- Resolve incidents quickly

**Food Shortage:**
- Build Farmsteads (2 Food each)
- Trade gold for food if desperate
- Reduce army size
- Check settlement consumption

**Incident Cascade:**
- Focus on reducing unrest below tier thresholds
- Use Fame for rerolls on critical incident checks
- Prioritize stability over growth during crisis

**Gold Shortage:**
- Build commerce structures for better trade rates
- Focus on economic development actions
- Complete beneficial events

---

## Notes

- Each simulation should use UNIQUE randomization
- Document any house rules or interpretations
- Note any software/tools used for dice rolling
- Keep the narrative engaging but accurate
- Focus on demonstrating the rules in action
- Track all incidents and their resolutions

**Remember:** The goal is to test whether the kingdom rules consistently produce balanced, enjoyable gameplay across multiple unique simulations while managing the tension between growth and stability through the unrest/incident system.

---

## Version History

- v1.0: Initial runner created from guidelines
- v2.0: Updated with new unrest tier system and incident mechanics
- [Future versions will be listed here]
