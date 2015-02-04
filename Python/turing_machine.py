"""
Turing Machine simulator driver
"""
from __future__ import print_function
import json
from turing_machine.Machine import Machine


def _main(machine_filename, tape):
    """
    Runs the turing machine simulator
    """
    with open(machine_filename) as json_file:
        json_data = json.load(json_file)
    tmachine = Machine(json_data)
    tmachine.set_tape(list(tape))
    if tmachine.run() is True:
        print("This was a valid TM")

if __name__ == "__main__":
    _main('tm_data/tm_01.json', "010#010")
    print("-----")
    _main('tm_data/tm_02.json', "00xx00")
