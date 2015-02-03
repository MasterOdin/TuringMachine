/*
  tmState
  
  Basic State of Turing Machine Object
*/

class tmState
{
  int currentState; // where are we in the state (for states with multiple routes out)
  String startState; // state name/number/whatever, technically not "startState", but rather just "stateName"
  // ArrayLists of what input do we accept, what we replace it with, what direction we move, and what state we then go to
  ArrayList read = new ArrayList();
  ArrayList replace = new ArrayList();
  ArrayList direction = new ArrayList();
  ArrayList nextState = new ArrayList();
  
  tmState(){  }
  
  // read in line, and add to the definitions of the node
  tmState(String readIn[])
  {
    startState = readIn[0];
    read.add(readIn[1]);
    replace.add(readIn[2]);
    direction.add(readIn[3]);
    nextState.add(readIn[4]);
  }

  void addLine(String readIn[])
  {
    read.add(readIn[1]);
    replace.add(readIn[2]);
    direction.add(readIn[3]);
    nextState.add(readIn[4]);
  }
  
  // returns for various class variables
  String getRead()
  {
    return (String) read.get(currentState);
  }
  
  String getReplace()
  {
    return (String) replace.get(currentState);
  }
  
  String getDirection()
  {
    return (String) direction.get(currentState);
  }
  
  String getNextState()
  {
    return (String) nextState.get(currentState);
  }

  String getStartState()
  {
    return startState;
  }

  /* what's the connection out of this state? */
  String getNext(String input)
  {
    for(int i = 0; i < read.size(); i++)
    {
      if(((String) read.get(i)).equals(input))
      {
        currentState = i;
        return (String) nextState.get(i);
      }
    }
    return "-1";
  }
  
  /* update input of the tape with state */
  String changeInput(String input,int iterator)
  {
    String begin = "";
    String a = input;
    iterator++;
    if(iterator <= input.length())
    {
      if(iterator > 1)
      {
        begin = input.substring(0,(iterator-1));
      }
      String str = input.substring(iterator);
      
      //println(iterator+": "+begin+"-"+((String) replace.get(currentState))+"-"+str);
      
      a = begin + ((String) replace.get(currentState)) + str;
    }
  
    return a;
    
  }
    
  void printStuff()
  {
    for(int i = 0; i < read.size(); i++)
    {
      print((String) startState+" "+(String) read.get(i)+" "+(String) replace.get(i)+" "+(String) direction.get(i)+" "+(String) nextState.get(i));
      println();
    }
  }
  
  void printTest()
  {
    print((String) startState+" "+(String) read.get(0)+" "+(String) replace.get(0)+" "+(String) direction.get(0)+" "+(String) nextState.get(0));
    println();
  }
  


}
