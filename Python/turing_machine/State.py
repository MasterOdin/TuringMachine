"""
Module providing a State for the Turing Machine
"""


class State(object):
    """
    Implementation of the Turing Machine state

    Attributes:
        name: Name of the state
        transitions: dictionary containing all the transition functions
    """
    def __init__(self, name):
        """
        Initialize the function
        :param name: State name
        """
        self.name = name
        self.transitions = dict()

    def add_transition(self, details):
        """
        Add a new transition function to the state
        :param details: transition function details (dictionary)
        """
        details['move_tape'] = details['move_tape'].lower()
        self.transitions[details['tape_symbol']] = details

    def get_transition(self, symbol):
        """
        Get the transition function for the symbol for the state
        :param symbol: symbol on the tape for the transition function
        :return: transition function details if exists, else raise KeyError
        """
        if symbol not in self.transitions:
            raise KeyError("No transition for " + symbol +
                           " in state " + self.name)
        else:
            return self.transitions[symbol]
