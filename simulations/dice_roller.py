#!/usr/bin/env python3
import random
from datetime import datetime

# Set seed for reproducibility
seed = datetime.now().strftime("%Y%m%d-%H%M%S")
random.seed(seed)

print(f"Simulation Seed: {seed}")
print("\nGenerating dice rolls for Kingdom Simulation #002")
print("="*50)

# Generate rolls for 50 turns
# Each turn needs multiple d20 rolls for various actions

turns = []
for turn in range(1, 51):
    turn_rolls = {
        'event_check': random.randint(1, 20),
        'pc1_action': random.randint(1, 20),
        'pc2_action': random.randint(1, 20),
        'pc3_action': random.randint(1, 20),
        'pc4_action': random.randint(1, 20),
        'companions': random.randint(1, 20),
        'extra_rolls': [random.randint(1, 20) for _ in range(3)]  # For events, rerolls, etc
    }
    turns.append(turn_rolls)

# Print rolls for each turn
for i, turn in enumerate(turns, 1):
    print(f"\nTurn {i} Rolls:")
    print(f"  Event Check: {turn['event_check']}")
    print(f"  PC1: {turn['pc1_action']}")
    print(f"  PC2: {turn['pc2_action']}")
    print(f"  PC3: {turn['pc3_action']}")
    print(f"  PC4: {turn['pc4_action']}")
    print(f"  Companions: {turn['companions']}")
    print(f"  Extra: {turn['extra_rolls']}")

# Generate some additional d20 rolls for events
print("\n" + "="*50)
print("Additional Event Rolls (d20):")
event_rolls = [random.randint(1, 20) for _ in range(20)]
for i in range(0, len(event_rolls), 5):
    print(f"  {event_rolls[i:i+5]}")

# Generate some d12 rolls for event types
print("\nEvent Type Rolls (d12):")
event_types = [random.randint(1, 12) for _ in range(10)]
print(f"  {event_types}")
