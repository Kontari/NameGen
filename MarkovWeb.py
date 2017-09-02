import random
#
# Trains Markov model to create names
#

class letter():

    def __init__(self, sh, w):
      self.out = sh
      self.weight = w


class MarkovWeb():
  
  def __init__(self, size ):
    self.states = consonants + vowel
    self.currState = NULL # State of markov model
    self.size = size # Number of states
      
  def setState():
    currState = random.randint(0, len(states) - 1)
        
  def stepState():
    # step state
    print "stall"
    
    
class State():
    
  def __init__(self, size , symbol ):
    self.size = size 
    self.stateShow = symbol.out
    self.states = consonants + vowel
    
    



def trainNodes( dataset ):
    print "trainNodes"
  

#
#############################################################################
#

consonants = [ letter("b",1), letter("c",1), letter("d",1), letter("f",1),
               letter("g",1), letter("h",1), letter("j",1), letter("k",1),
               letter("l",1), letter("m",1), letter("n",1), letter("p",1),
               letter("q",1), letter("r",1), letter("s",1), letter("t",1),
               letter("v",1), letter("w",1), letter("x",1), letter("y",1),
               letter("z",1) ]
vowel = [ letter("a",1), letter("e",1),
          letter("i",1), letter("o",1), 
          letter("u",1) ]
          
          
          
