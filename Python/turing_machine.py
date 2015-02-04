"""
Turing Machine simulator driver
"""

import json
from turing_machine.Machine import Machine


def _main():
    """
    Runs the turing machine simulator
    """
    with open('tm_data/tm_01.json') as json_file:
        json_data = json.load(json_file)
    tmachine = Machine(json_data)
    tmachine.set_tape(list("010#010"))
    if tmachine.run() is True:
        print("This was a valid TM")

if __name__ == "__main__":
    _main()
