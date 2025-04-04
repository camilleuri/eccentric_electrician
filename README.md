# The Eccentric Electrician

This is a Python library that simulates the logic of the Eccentric Electrician puzzle.

### The Puzzle

An eccentric electrician has wired n lights, all initially on, so that:

1) light 1 can always be turned on/off, and
2) light k cannot be turned either on or off unless light k – 1 is on and all preceding lights are off for k > 1.

How many moves are required to turn all n lights off?

### Usage Example

```python
from eccentric_electrician import Puzzle

p = Puzzle(3)

p.game_state()
p.check_puzzle()

p.flip_switch(0)
p.flip_switch(2)
p.flip_switch(0)
p.flip_switch(1)
p.flip_switch(0)

p.game_state()
p.check_puzzle()
```

Output:

```
Puzzle initialized with 3 switches in the on position.
Current game state: ['on', 'on', 'on']
Puzzle is unsolved.
Flip! Switch 0 is now off.
Flip! Switch 2 is now off.
Flip! Switch 0 is now on.
Flip! Switch 1 is now off.
Flip! Switch 0 is now off.
Current game state: ['off', 'off', 'off']
Puzzle is solved!
```

See examples.py for more examples.

### Functions

> Note: Switch numbering starts at 0.

``Puzzle(num_switches, starting_pos="on", verbose=True)`` - Initializes a puzzle with num_switches, all set to starting_pos. If verbose is True, the puzzle will print your moves and checks automatically.

``flip_switch(switch)`` - Attempt to flip switch at index switch. Returns True if the switch is successfully flipped, and False if the switch cannot be flipped.

``check_switch(switch)`` - Checks the state of the switch at index switch. Returns True if the switch is on, and False if the switch is off.

``game_state()`` - Checks the overall state of the game. Returns a list of switches, either "on" or "off".

``check_puzzle()`` - Checks if the puzzle is solved. Returns True if so, and False if not.

Extra functions, mostly for internal use:

``resolve_bool(state)`` - Resolves a boolean to either "on" or "off".

``resolve_str(state)`` - Resolves "on" or "off" to a boolean.

``cprint(string)`` - Prints string if verbose is True.