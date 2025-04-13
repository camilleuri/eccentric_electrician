class Puzzle:

    def __init__(self, num_switches, starting_pos="on", verbose=True, console=False):
        self.switch_count = num_switches
        self.switches = []
        self.win_condition = not self.resolve_str(starting_pos)
        self.flip_count = 0
        self.verbose = verbose
        self.console = console

        for i in range(self.switch_count):
            self.switches.append(self.resolve_str(starting_pos))
        self.cprint("Puzzle initialized with " + str(self.switch_count) + " switches in the " + starting_pos + " position.")

    def cprint(self, string): # Conditional print - only print if puzzle is in verbose mode
        if self.verbose:
            print(string)

    def resolve_bool(self, state): # For internal use, resolves boolean to on/off string
        if state:
            return "on"
        else:
            return "off"
        
    def resolve_str(self, state): # For internal use, resolves on/off string to boolean
        if state.lower() == "on":
            return True
        else:
            return False

    def check_switch(self, switch): # Check if a switch is on or off
        if self.switches[switch]:
            self.cprint("Switch #" + str(switch) + " is on.")
            if not self.console: return True
        else:
            self.cprint("Switch #" + str(switch) + " is off.")
            if not self.console: return False
        
    def flip_switch(self, switch): # Toggle switch, if possible
        if switch < 1 or switch >= self.switch_count: # Special cases
            if switch == 0: # First switch
                self.switches[0] = not self.switches[0]
                self.cprint("Flip! Switch 0 is now " + self.resolve_bool(self.switches[0]) + ".")
                self.flip_count += 1
                if not self.console: return True
            else: # Out of bounds
                self.cprint("Error: Out of bounds. Valid switches: 0-" + str(self.switch_count-1) + ". You tried: " + str(switch) + ".")
                if not self.console: return False
        else: # In bounds switch 1-n
                if self.switches[switch-1] and not True in self.switches[:switch-1]:
                    self.switches[switch] = not self.switches[switch]
                    self.cprint("Flip! Switch " + str(switch) + " is now " + self.resolve_bool(self.switches[switch]) + ".")
                    self.flip_count += 1
                    if not self.console: return True
                else:
                    self.cprint("Error: Could not flip switch " + str(switch) + " due to failed conditions.")
                    if not self.console: return False

    def game_state(self): # Print current state of game
        current_state = []
        for switch in self.switches:
            current_state.append(self.resolve_bool(switch))
        self.cprint("Current game state: " + str(current_state))
        if not self.console: return current_state

    def check_puzzle(self): # Check if puzzle is solved
        if (not self.win_condition) in self.switches:
            self.cprint("Puzzle is unsolved.")
            if not self.console: return False
        else:
            self.cprint("Puzzle is solved!")
            if not self.console: return True
