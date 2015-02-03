Turing Machine Simulator
By Matthew Peveler
For CSC460 - Theory of Computation

~~README~~
The program requires Processing (http://www.processing.org) to run. It was made on v2.05a, but should work on the current stable release (1.5).
The main program file is "TM_Simulator.pde" with the "tmState.pde" being a class definition for a state in the TM network.

For simple execution, open the "TM_Simulator.exe" to run the simulator based onthe contents of the two text files specified below.  There is also a
"TM_Simulator" file that should run on Linux, but compatibility and usability cannot be guaranteed. Running through Process will of course always work.

The program will simulate a TM given an input and a set of states in the following two text files:
"tm_states.txt" - States for the transitions in the TM
"tm_input.txt" - Input that the TM will read in

Note: Both text files must exist in teh same directory as the executing program/processing sketch file. No real error checking was done on the files,
		so the behavior of the program is undefined at best if trying to run the program without those files.

The program will only consider what is in the input, and perform actions on that. If the head of the iterator
on the tape exceeds the length of the input, it is not an accept state, the TM will add a _ (white space) to the end of the input
as neccessary, so long as it hasn't entered an accept/reject state.


"Test States.txt" contains a list of states for two different TM simulations to try out the program easily, as both are confirmed to:
a) work
b) are examples from the Theory of Compuation textbook


~~LICENSE~~
This is licensed under the MIT license, the text of which can be found under ../LICENSE

~~FILE FORMATS~~
tm_states.txt format:
<current state> <current symbol> <new symbol> <direction> <next state>

If next state is an accept state, simply put "a" instead of a state corresponding to another state. If the next state is a reject state, simply put a "r"

<direction> should "l"/"L" for Left and "r"/"R" for Right.. It can be lower case or upper case.

For any state transitions where the input is not affected, just put the same symbol in the 2nd and 3rd categories.

The first state read into the file is the "start state" and will be where the TM will begin. q0 is implicit in that it feeds to
the first listed q immediately. 

tm_input.txt:
Input string to read into by the TM. Empty spaces are to be written as _. Accepts most characters found on US keyboard. Only tested for 0,1,#, and *, but should work for most
keys on a standard US keyboard.