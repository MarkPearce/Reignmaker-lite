# Unrest

Unrest represents the dissatisfaction, tension, and disorder within your kingdom. Rather than simply making all actions harder through escalating penalties, unrest creates specific crises and consequences that demand attention. The penalty progression is gentler, but the narrative and mechanical consequences become increasingly severe through incident rolls.

## Core Philosophy

The unrest system creates dynamic challenges that require strategic response rather than simply imposing ever-increasing penalties. As unrest rises, your kingdom faces specific incidents—from minor crime waves to full-scale rebellions—that test different skills and create meaningful choices about resource allocation and crisis management.

## Unrest Tiers and Effects

| Tier | Name | Unrest Range | Penalty | Incident Table (d100) | Description |
|------|------|--------------|---------|----------------|-------------|
| **0** | **Stable** | 0-2 | None | None | The kingdom is content and functioning normally |
| **1** | **Discontent** | 3-5 | -1 to all checks | Minor Incidents | Growing dissatisfaction requires attention |
| **2** | **Turmoil** | 6-8 | -2 to all checks | Moderate Incidents | Serious unrest threatens stability |
| **3** | **Rebellion** | 9+ | -3 to all checks | Major Incidents | Open revolt endangers the kingdom |

*See Unrest_incidents.md for complete incident tables*

## Common Sources of Unrest

**Failed Actions - Selective Consequences:**
Only certain critical failures on specific actions cause +1 Unrest:

- **Crisis Response Actions:** Resolve Kingdom Event, Deal with Unrest, Execute/Pardon Prisoners
- **Military Operations:** Recruit Army, Deploy Army, Disband Army  
- **Public Order:** Arrest Dissidents
- **Other actions (development, economic, etc.):** No unrest on critical failure

**Resource Shortages:**
- Unfed settlement: Unrest equal to settlement tier (Village: +1, Town: +2, City: +3, Metropolis: +4)
- Unfed army: +1 Unrest per army without food
- Unsupported armies: +1 Unrest per excess army each turn

**Military Issues:**
- Failed army morale checks: +1 Unrest (or +2 on critical failure)
- Army disbanding: +1 Unrest (or +2 if through mutiny/desertion)

**Other Sources:**
- Being at war: +1 Unrest per turn
- Unresolved kingdom events
- Certain narrative consequences
- Hex-based generation: +1 per 8 hexes controlled
- Metropolis complexity: +1 per Metropolis

## Imprisoned Unrest

Imprisoned Unrest represents dissidents, troublemakers, and malcontents who have been detained by your justice system. This unrest is stored separately and does not count toward your kingdom's total Unrest penalties.

- **Storage:** Imprisoned Unrest is held in settlements with Justice structures (Courts, Tribunals, etc.)
- **Not Counted:** Does not contribute to kingdom roll penalties while imprisoned
- **Resolution:** Can be dealt with through the Execute or Pardon Prisoners action
- **Risk:** If not addressed, may escape or cause problems through events

## Reducing Unrest

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

## Incident Roll Mechanics

**When:** At the start of each Kingdom Turn (Phase 2), after calculating current unrest tier

**Action Economy:** Incidents do NOT consume Kingdom Actions - they are immediate crises that must be resolved with a skill check

**Who Rolls:** The kingdom rolls on the appropriate incident table based on tier:
- **Tier 0 (0-2):** No roll
- **Tier 1 (3-5):** Roll d100 on Minor Incidents table
- **Tier 2 (6-8):** Roll d100 on Moderate Incidents table
- **Tier 3 (9+):** Roll d100 on Major Incidents table

**No Incident Results:**
- Minor Incidents: 20% chance (01-20)
- Moderate Incidents: 15% chance (01-15)
- Major Incidents: 10% chance (01-10)

**Resolution Process:**
1. **Roll for Incident:** Determine which incident occurs
2. **Choose Approach:** Select which skill to use from the incident's options
3. **Make Skill Check:** One PC rolls using Level-based DC
4. **Apply Results:** Based on success/failure degree

**Important:** Resolving an incident requires a skill check but does NOT consume a Kingdom Action. These are immediate crises that interrupt normal kingdom business. All incidents resolve immediately - there are no ongoing or persistent incidents.

**Incident Tables:** For the complete list of incidents with descriptions, skill checks, and effects, see **Unrest_incidents.md**

## Recovery Strategies

Different tiers require different approaches:
- **Tier 0:** No action needed - kingdom is stable
- **Tier 1:** Standard unrest management, preventive measures
- **Tier 2:** Active crisis management, moderate incidents
- **Tier 3:** Emergency measures required, major incidents and possible territorial losses
