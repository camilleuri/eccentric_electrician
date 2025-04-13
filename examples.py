from eccentric_electrician import Puzzle
from random import randint

# Example mutually recursive solution

def turn_on(p, n):
    if n == 0: p.flip_switch(0); return

    turn_on(p, n-1)
    if n > 1: turn_off(p, n-2)
    p.flip_switch(n)
    if n > 1: turn_on(p, n-2)
    

def turn_off(p, n):
    if n == 0: p.flip_switch(0); return

    if n > 1: turn_off(p, n-2)
    p.flip_switch(n)
    if n > 1: turn_on(p, n-2)
    turn_off(p, n-1)

p = Puzzle(10)
turn_off(p, 9)
print(p.flip_count)

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

i = 0

e = Puzzle(5, starting_pos="on", verbose=False)
while not e.check_puzzle():
    e.flip_switch(randint(0, p.switch_count-1))
    i += 1

print("Random tries required to solve:", i, "\nSwitches flipped successfully:", e.flip_count)
