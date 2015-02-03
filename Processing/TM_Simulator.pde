/**
  Turing Machine Simulator
  Matthew Peveler
  CSC460
  4/29/2012
  
  Simulates a Turing Machine, reading in the states from data/tm_states.txt and the input from data/tm_input.txt
*/


// initialize variables
String currentState = "n"; //state we're currently working on
String originalState; // save the first state for resetting
HashMap hm; // get where we save a state in the states array

String input;
String original;

int iterator = 0;

boolean done = false;
boolean failed = false;

tmState states[];
int stateCount = 0;
int stateMap[];

int currentWidth = 0;

int it = 0; // index of the states[] we're using
int fr = 4; // frame rate

void setup()
{
  frame.setResizable(true);
  frameRate(fr);

  PFont font;
  font = loadFont("HelveticaCE-Regular-24.vlw");
  textFont(font);  
  
  String use;
  /* load in input, save it to original so we can't lose it */
  String lines[] = loadStrings("tm_input.txt");
  input = lines[0];
  original = input;
  
  /* load in states */
  lines = loadStrings("tm_states.txt");
  String tmp[];
  hm = new HashMap<String,tmState>();
  tmState tmpState;
  int count = 0;
  
  // get all states, making sure to add duplicates to existing mappings. get cout for states[] array initalization
  for(int i = 0; i < lines.length; i++)
  {
    tmp = splitTokens(lines[i]," ");
    if(currentState.equals("n"))
    {
      currentState = tmp[0];
      originalState = currentState;
    }    
    if(!hm.isEmpty())
    {
      tmpState = new tmState();
      
      if(!hm.containsKey(tmp[0]))
      { 
        tmpState = new tmState(tmp);
        count++;
      }
      else
      {
        tmpState = (tmState) hm.get(tmp[0]);
        tmpState.addLine(tmp);
      }
    }
    else
    {
        tmpState = new tmState(tmp);
        count++;
    }
    hm.put(tmp[0],tmpState);
  }

  // iterate through hashmap, finally setting up states array
  Iterator i = hm.entrySet().iterator();
  
  stateCount = count;
  count = 0;
  
  states = new tmState[stateCount];
  stateMap = new int[stateCount];
  
  i = hm.entrySet().iterator();
  while(i.hasNext()) {
    Map.Entry entry = (Map.Entry) i.next();
    tmpState = (tmState) entry.getValue();
    states[count++] = tmpState;
  }
  
  // create link between where in states a specific state is with mapping
  hm.clear();
  hm = new HashMap<String,Integer>();
  for(int j = 0; j < stateCount; j++)
  {
    hm.put(states[j].getStartState(), j);
  }
  
  if((40*input.length()) > 500)
  {
    size((40*input.length()),600);
  }
  else
  {
    size(500,600);
  }
  currentWidth = width;
}

/* resize window (should only happen if input increases to new _ character */

void reSize()
{
  if((40*input.length()) > 500 && currentWidth != (41*input.length()))
  {
    frame.setSize((40*input.length()),638);
  }
  else
  {
    if(currentWidth != 500)
    {
      frame.setSize(500,638);
    }
  }
  currentWidth = width;
  
}

/* restart routine */
void restart()
{
  input = original;
  iterator = 0;
  done = false;
  failed = false;  
  currentState = originalState;
  fr = 4;
  frameRate(fr);
  
}

void draw()
{
  /* DRAWING */
  background(233,233,233);
  fill(0);
  
  textSize(16);
  text("Speed: "+fr,(width-90),20);
  
  textSize(32);
  text("Turing Machine Simulator",10,40);
  textSize(26);
  text("By Matthew Peveler",150,75);
  
  textSize(24);
  String direction;
  tmState getState;
  int neededState;

  // need to increase iterator to have arrow be right, who knew
  String str = "_";
  if(!failed)
  {
    if((iterator+1 > input.length()) && !done)
    {
      input = input + "_";
      reSize();     
    } 
    
    if(!done) 
      str = input.substring(iterator,(iterator+1));
  }
  

  
  text("Status: ",40,440);
  
  if(failed)
  {
    text("State: qr",40,320);
    fill(255,0,0);
    text("REJECTED",125,440);
    noLoop();
  }
  else if(done)
  {
    text("State: qa",40,320);
    fill(0,100,0);
    text("ACCEPTED",125,440);
    noLoop();
  }
  else
  {
    text("Ongoing",125,440);
  }  

  //println(str);
  
  /* DRAWING */
  fill(0);
  text("^",(30*(iterator+1))+10,280);
  text("Original:",10,130);
  text("Input:",10,220);
  fill(255);
  stroke(0);
  for(int j = 0; j < input.length(); j++)
  {
    if(j < original.length())
    {
      fill(255);
      rect((30*(j+1)),140,30,30);
      fill(0);
      text(original.charAt(j)+" ",(30*(j+1))+10,165);
    }
    
    fill(255);
    rect((30*(j+1)),230,30,30);
    fill(0);
    text(input.charAt(j)+" ",(30*(j+1))+10,255);
  }
  
  
  /* LOGIC */
  /* Get current state we're on, then find out what the next state is (in case it's a reject/accept, as well as what connection
      we're following out of the current state). Then change position of track head if going r(ight) or l(left) */
  if(!done && !failed)
  {
    Object p = hm.get(currentState);
    it = (Integer) p;
    
    /* LOGIC */
    //println(states[m].getStartState());
    currentState = states[it].getNext(str);
    if(!currentState.equals("-1"))
    {
      input = states[it].changeInput(input,iterator);
      direction = states[it].getDirection();
      if(direction.toLowerCase().equals("l"))
      {
        iterator--;
      }
      else if(direction.toLowerCase().equals("r"))
      {
        iterator++;
      }
      
      if(currentState.equals("r"))
      {
        failed = true;
      }
      else if(currentState.equals("a"))
      {
        done = true;
      }
    }
    else
    {
      failed = true;
    }
    
     /* DRAWING */
    text("State: q"+states[it].getStartState(),40,320);
    text("Next: "+states[it].getRead()+" -> "+states[it].getReplace()+","+states[it].getDirection().toUpperCase()+" to q"+states[it].getNextState(),40,370);    
  }

  textSize(16);
  fill(0);
  text("Any key to exit simulation",40,530);
  
  if(!failed && !done)
  {
    text("Left mouse click to slow down.",40,550);
    text("Right mouse click to speed up.",40,570);
  }
  else
  {
    text("Press any mouse button to restart.",40,550);
  }
}

/* decrease/increase speed of simulation. Or restart if simulation finished. */
void mousePressed()
{
  if(!failed && !done)
  {
    if(mouseButton == LEFT)
    {
      fr = (fr-2<2) ? 2 : fr-2;
    }
    if(mouseButton == RIGHT)
    {
      fr += 2;
    }
    frameRate(fr);
  }
  else
  {
    restart();
    loop();
  }
  //exit();
}

/* simple way to exit() */
void keyPressed()
{
  if(1 == 1)
  {
      exit();
  }
}

