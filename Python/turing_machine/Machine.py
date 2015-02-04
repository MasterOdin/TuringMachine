"""
Module which provides a turing machine
"""
# pylint: disable=too-many-instance-attributes

from __future__ import print_function
from turing_machine.State import State


class Machine(object):
    """
    Implementation of the Turing Machine

    Attributes:
        no_shift: allow the 'n' (no shift) move symbol in transition function
        states: dictionary that contains all the states of the TM
        alphabet: alphabet that's available in the TM
        blank: blank symbol to be used by the TM
        initial: The start state of the TM
        final_states: The final states that produce an Accept reply
        tape: The tape of the current running Machine
        original_tape: The tape that was originally fed to the machine
        tape_index: The position of the head on the TM tape
        current_state: Current state that the TM is in
    """
    no_shift = False

    def __init__(self, details):
        """
        Create the TM machine
        :param details: Dictionary containing the implementation details
                        of the TM
        """
        self.states = dict()
        for state in details['states']:
            self.states[state] = State(state)
        self.alphabet = details['alphabet']
        self.blank = details['blank']
        self.initial = details['initial_state']
        self.final_states = details['final_states']
        self.tape = []
        self.original_tape = []
        self.tape_index = 0

        for transition in details['transition_functions']:
            self.check_transition(transition)
            self.states[transition['state']].add_transition(transition)
        self.current_state = self.initial

    def reset_machine(self):
        """
        Reset the machine back to its initial state and tape
        """
        self.tape = self.original_tape
        self.tape_index = 0
        self.current_state = self.initial

    def check_transition(self, trans):
        """
        Check a transition function to ensure it's valid in that it doesn't
        reference a state that doesn't exist or an invalid symbol
        :param trans: dictionary containing the transition function details
        :return: True if valid transition, else raise KeyError
        """
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
        """
        Set the tape for current run of the TM
        :param tape: String/List that contains the Tape details
        """
        if isinstance(tape, str):
            self.tape = list(tape)
        else:
            self.tape = tape
        self.original_tape = tape
        self.tape_index = 0

    def check_finished(self):
        """
        Check if the TM is in a finished state
        :return: True if we are in final_states, else False
        """
        return self.current_state in self.final_states

    def run(self):
        """
        Run the TM till it halts in success/failure
        :return: True if TM halts and suceeds, else raise KeyError on invalid
                 Tape
        """
        while self.check_finished() is False:
            symbol = self.get_symbol()
            print(self.current_state, self.tape_index, self.tape_str())
            trans = self.states[self.current_state].get_transition(symbol)
            self.write_symbol(trans['write_symbol'])
            self.shift_tape(trans['move_tape'])
            self.current_state = trans['next_state']
        return True

    def get_symbol(self):
        """
        Get symbol from the tape on where the head (tape_index) is
        :return: character at the index on the tape
        """
        if self.tape_index >= len(self.tape):
            return self.blank
        else:
            return self.tape[self.tape_index]

    def write_symbol(self, symbol):
        """
        Write the symbol from the transition function to the tape at the
        current index
        :param symbol: character to write onto the tape at index
        """
        if self.tape_index >= len(self.tape):
            self.tape.append(symbol)
        else:
            self.tape[self.tape_index] = symbol

    def shift_tape(self, shift):
        """
        Shift the tape index left/right based off transition function. If we
        shift past the stored tape, prepend/append a blank symbol to it
        :param shift: shift symbol from transition funciton
        """
        shift = shift.lower()
        if shift == 'r':
            self.tape_index += 1
            if self.tape_index >= len(self.tape):
                self.tape += [self.blank]
        elif shift == 'l':
            self.tape_index -= 1
            if self.tape_index < 0:
                self.tape = [self.blank] + self.tape

    def tape_str(self):
        """
        Convert the Tape from a list to a str
        :return: string version of the tape
        """
        return "".join(self.tape)
