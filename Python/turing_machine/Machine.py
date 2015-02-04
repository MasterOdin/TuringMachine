"""
The main hardware of the Turing Machine, storing the states
and other necessary data
"""
# pylint: disable=too-many-instance-attributes

from turing_machine.State import State


class Machine(object):
    no_shift = False

    def __init__(self, details):
        self.states = dict()
        for state in details['states']:
            self.states[state] = State(state)
        self.alphabet = details['alphabet']
        self.blank = details['blank']
        self.initial = details['initial_state']
        self.final_states = details['final_states']
        self.tape = []
        self.tape_index = 0

        for transition in details['transition_functions']:
            self.check_transition(transition)
            self.states[transition['state']].add_transition(transition)
        self.current_state = self.initial

    def check_transition(self, trans):
        valid_moves = ['l', 'r'] + (['r'] if self.no_shift is True else [])
        if trans['state'] not in self.states:
            raise KeyError("The state '" + trans['state'] +
                           "' was not defined in the formal tuple")
        if trans['next_state'] not in self.states:
            raise KeyError("The state '" + trans['next_state'] +
                           "' was not defined in the formal tuple")
        if trans['move_tape'].lower() not in valid_moves:
            raise KeyError(trans['move_tape'] + " is not a "
                                                "valid tape move")
        if (trans['tape_symbol'] not in self.alphabet and
                trans['tape_symbol'] != self.blank):
            raise KeyError(trans['tape_symbol'] + " is not in the alphabet"
                           " and is an invalid tape_symbol")
        if (trans['write_symbol'] not in self.alphabet and
                trans['write_symbol'] != self.blank):
            raise KeyError(trans['write_symbol'] + " is not in the alphabet"
                           " and is an invalid write_symbol")

        return True

    def set_tape(self, tape):
        if isinstance(tape, str):
            self.tape = list(tape)
        else:
            self.tape = tape

    def check_finished(self):
        return self.current_state in self.final_states

    def run(self):
        while self.check_finished() is False:
            symbol = self.get_symbol()
            #print(self.current_state, self.tape_index, self.tape)
            trans = self.states[self.current_state].get_transition(symbol)
            self.write_symbol(trans['write_symbol'])
            if trans['move_tape'] == 'r':
                self.tape_index += 1
            elif trans['move_tape'] == 'l':
                self.tape_index -= 1

            self.current_state = trans['next_state']

        return True

    def get_symbol(self):
        if self.tape_index >= len(self.tape):
            return self.blank
        else:
            return self.tape[self.tape_index]

    def write_symbol(self, symbol):
        if self.tape_index >= len(self.tape):
            self.tape.append(symbol)
        else:
            self.tape[self.tape_index] = symbol
