from eccentric_electrician import Puzzle

# Example hardcoded solution to n = 5, lights on to start

p = Puzzle(5, "on")

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