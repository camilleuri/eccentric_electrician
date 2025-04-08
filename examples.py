from eccentric_electrician import Puzzle
from random import randint

# Example hardcoded solution to n = 5, lights off to start

p = Puzzle(5, "off")

p.check_puzzle()

p.flip_switch(0)
p.flip_switch(1)
p.flip_switch(0)
p.flip_switch(2)

p.flip_switch(0)
p.flip_switch(1)
p.flip_switch(0)
p.flip_switch(3)

p.flip_switch(0)
p.flip_switch(1)
p.flip_switch(0)
p.flip_switch(2)

p.flip_switch(0)
p.flip_switch(1)
p.flip_switch(0)
p.flip_switch(4)

p.flip_switch(0)
p.flip_switch(1)
p.flip_switch(0)
p.flip_switch(2)

p.flip_switch(0)

p.game_state()
p.check_puzzle()

# Example bogosort-like solve, flip random switches until solved.

size = 5
i = 0

e = Puzzle(size, starting_pos="on", verbose=False)
while not e.check_puzzle():
    e.flip_switch(randint(0, size-1))
    i += 1

print("Random flips required to solve:", i)
