# Kingdom Simulation Runner for Reignmaker-lite

## Purpose
This document serves as a simulation runner for the Reignmaker-lite subsystem for pathfinder. Each time you run this simulation, it will:
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

3. **Create new simulation file:**
   - Filename: `kingdom_simulation_###.md` (e.g., kingdom_simulation_001.md)
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

**Player Characters:**
- 4 PCs at Level 4 (starting level)
- Companions available for collective action
- 2 PCs with Expert proficiency (+11) in their primary skill
- 2 PCs with Trained proficiency (+8) in their primary skill

---

## Core Mechanics

### Kingdom Level = Party Level
The kingdom level advances in lockstep with the party level. They are the same number.

### DC Structure
**ALL kingdom actions use On-Level DCs:**
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

### Dice Resolution
**Use actual d20 rolls for each check:**
- Roll: 1d20 + modifier vs DC
- **Critical Success:** Beat DC by 10+ OR natural 20
- **Critical Failure:** Fail DC by 10+ OR natural 1
- **Success:** Meet or exceed DC (without critical)
- **Failure:** Below DC (without critical)

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
- Gain 1 Fame (if not at max)
- Note available Fame for rerolls

### Phase 2: Apply Modifiers
- Check if at war (+1 Unrest if yes)
- Apply structure bonuses
- Calculate Unrest penalty (-1 per 5 Unrest)

### Phase 3: Kingdom Event Check
- Start at DC 16
- Reduce by 5 each turn without event
- Reset to DC 16 after event occurs
- Roll d20 vs DC

### Phase 4: Resource Management
- Calculate production from all worksites
- Subtract consumption (settlements + armies)
- Apply storage limits
- Process construction projects

### Phase 5: Kingdom Actions
- Each PC takes one action
- Companions take one collective action
- Apply all modifiers and roll d20 for each
- Record actual roll, modifier, total, and result type

### Phase 6: End of Turn
- Update all kingdom statistics
- Check for milestone achievements
- Note any special conditions

---

## Turn Tracking Template

```markdown
## Turn [X] - Party Level [Y]
**Simulation Seed:** [Your unique seed/timestamp]

### Phase 1: Gain Fame
- Starting Fame: [X]
- Gained: +1
- Total: [X]

### Phase 2: Apply Modifiers
- At War: [Yes/No]
- Structure Bonuses: [List]
- Unrest: [X] (Penalty: -[Y])

### Phase 3: Kingdom Event
- DC: [Current DC]
- Roll: [d20 result]
- Event: [None/Event Type]

### Phase 4: Resources
**Production:**
- Food: +[X] ([sources])
- Lumber: +[X] ([sources])
- Stone: +[X] ([sources])
- Ore: +[X] ([sources])

**Consumption:**
- Settlements: -[X] Food
- Armies: -[X] Food
- Net: [+/- amounts]

**Storage:**
- Food: [X]/[Max]
- Gold: [X]
- Resources: [List]

### Phase 5: Kingdom Actions
1. PC1 (Expert +11): [Action]
   - Roll: [d20]+11 = [Total] vs DC 19
   - Result: [Critical Failure/Failure/Success/Critical Success]
   - Effect: [What happened]

2. PC2 (Expert +11): [Action]
   - Roll: [d20]+11 = [Total] vs DC 19
   - Result: [Type]
   - Effect: [What happened]

3. PC3 (Trained +8): [Action]
   - Roll: [d20]+8 = [Total] vs DC 19
   - Result: [Type]
   - Effect: [What happened]

4. PC4 (Trained +8): [Action]
   - Roll: [d20]+8 = [Total] vs DC 19
   - Result: [Type]
   - Effect: [What happened]

5. Companions: [Action]
   - Roll: [d20]+[Mod] = [Total] vs DC 19
   - Result: [Type]
   - Effect: [What happened]

### Phase 6: Summary
- Hexes: [X]
- Settlement: [Type and Level]
- Armies: [X]
- Unrest: [X]
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

### Turn 20 (Level 8)
Expected Status:
- Town Level 3-4
- 10-14 hexes controlled
- 5-6 worksites active
- 4-5 structures built
- 1-2 armies

### Turn 30 (Level 10)
Expected Status:
- City (Level 5+)
- 15-20 hexes controlled
- 7-9 worksites active
- 6-7 structures built
- 2-3 armies

### Turn 40 (Level 12)
Expected Status:
- City Level 6-7
- 20-25 hexes controlled
- 10-12 worksites active
- 8-9 structures built
- 3-4 armies

### Turn 50 (Level 15)
Expected Status:
- Metropolis (Level 8+)
- 25-30 hexes controlled
- 13-15 worksites active
- 10-12 structures built
- 4-5 armies

---

## Success Metrics

Evaluate each simulation against these targets:

### Minimum Success
- [ ] Town achieved (Level 2+)
- [ ] 15+ hexes controlled
- [ ] Unrest never exceeded 10
- [ ] No settlement lost
- [ ] Positive gold balance

### Standard Success
- [ ] City achieved (Level 5+)
- [ ] 20-25 hexes controlled
- [ ] Average unrest below 5
- [ ] Won at least 1 conflict
- [ ] 50+ gold accumulated

### Exceptional Success
- [ ] Metropolis achieved (Level 8+)
- [ ] 30+ hexes controlled
- [ ] Average unrest below 3
- [ ] Multiple victories
- [ ] 100+ gold accumulated

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

### Critical Failure Effects
- **Development:** No progress + damage
- **Resources:** Loss or accident
- **Military:** Desertion or defeat
- **Diplomacy:** War or embargo
- **Crisis:** Escalation + new problem

---

## Action Priority Guidelines

When deciding PC actions each turn:

### Crisis Priority (Unrest 5+)
1. Deal with Unrest
2. Address root causes
3. Build stability structures

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

## Simulation Output Format

Your simulation file should include:

### Header
```markdown
# Kingdom Simulation #[Number]
**Date:** [When run]
**Seed:** [Unique identifier]
**Runner:** [Who ran it]
**Result:** [Success level achieved]
```

### Summary Statistics
- Final settlement level
- Total hexes controlled
- Gold accumulated
- Armies maintained
- Structures built
- Critical successes/failures
- Unrest incidents

### Turn Logs
- Detailed record of all 50 turns
- Key decision points noted
- Critical moments highlighted

### Analysis Section
- Comparison to expected milestones
- Notable deviations
- Strategic insights
- Recommendations

---

## Post-Simulation Checklist

After completing your simulation:

1. **Save simulation file** as `kingdom_simulation_###.md`

2. **Update master analysis** in `kingdom_system_analysis.md`:
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

### Settlement Levels
- Level 0: Village
- Level 1: Village+
- Level 2-4: Town
- Level 5-7: City  
- Level 8+: Metropolis

### Structure Tiers
- T1: Village structures
- T2: Town structures
- T3: City structures
- T4: Metropolis structures

### Army Costs
- Recruit: 1 action
- Maintain: 1 Food/turn
- Capacity: Based on structures

### Resource Storage (without structures)
- Food: 12 (Granary: +12)
- Gold: Unlimited
- Materials: 0 (need Storehouse)

---

## Troubleshooting

### Common Issues

**Unrest Spiral:**
- Prioritize Deal with Unrest
- Build Theater/cultural structures
- Avoid critical failures

**Food Shortage:**
- Build more Farmsteads
- Trade for food
- Reduce army size

**Expansion Stall:**
- Wait for Master proficiency (Level 7)
- Use Coordinated Actions
- Focus on other growth

**Gold Shortage:**
- Build economic structures
- Focus on Trade actions
- Develop settlements for taxes

---

## Notes

- Each simulation should use UNIQUE randomization
- Document any house rules or interpretations
- Note any software/tools used for dice rolling
- Keep the narrative engaging but accurate
- Focus on demonstrating the rules in action

**Remember:** The goal is to test whether the kingdom rules consistently produce balanced, enjoyable gameplay across multiple unique simulations.

---

## Version History

- v1.0: Initial runner created from guidelines
- [Future versions will be listed here]
