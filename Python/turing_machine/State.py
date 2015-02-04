"""
A state in our turning machine
"""


class State(object):
    def __init__(self, name):
        self.name = name
        self.transitions = dict()

    def add_transition(self, details):
        details['move_tape'] = details['move_tape'].lower()
        self.transitions[details['tape_symbol']] = details

    def get_transition(self, symbol):
        if symbol not in self.transitions:
            raise KeyError("No transition for " + symbol +
                           " in state " + self.name)
        else:
            return self.transitions[symbol]