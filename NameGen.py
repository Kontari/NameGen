import random
#
# Generates names using pseudo-machine learning
#

'''
BACKUP

consonants = [ letter("b",1), letter("c",1), letter("d",1), letter("f",1),
               letter("g",1), letter("h",1), letter("j",1), letter("k",1),
               letter("l",1), letter("m",1), letter("n",1), letter("p",1),
               letter("q",1), letter("r",1), letter("s",1), letter("t",1),
               letter("v",1), letter("w",1), letter("x",1), letter("y",1),
               letter("z",1) ]

vowel = [ letter("a",1), letter("e",1),
          letter("i",1), letter("o",1), 
          letter("u",1) ]
'''

class letter():

    def __init__(self, sh, w):
        self.out = sh
        self.weight = w

consonants = [ letter("b",3), letter("c",3), letter("d",8), letter("f",4),
               letter("g",4), letter("h",12), letter("j",1), letter("k",2),
               letter("l",8), letter("m",5), letter("n",13), letter("p",4),
               letter("q",1), letter("r",12), letter("s",13), letter("t",18),
               letter("v",2), letter("w",4), letter("x",1), letter("y",4),
               letter("z",1) ]

vowel = [ letter("a",16), letter("e",24),
          letter("i",14), letter("o",15), 
          letter("u",5) ]
        
#def trainData( filename ) :

# Pick a letter from the list passed in
def pickOne( options ) : 

    totalWeight = 0

    # Find the total of weights
    for x in range(0, len(options) ):
    	totalWeight += options[x].weight

    randSelect = random.randint(1 , totalWeight)

    #print "Selection: " + str(randSelect)

    totalWeight = 0

    for x in range(0, len(options) - 2):

    	if ( randSelect >= totalWeight and randSelect < (totalWeight + options[x + 1].weight ) ) :
            return options[x].out

        totalWeight += options[x].weight    

    return pickOne( options )



# Takes in a string of cv's
def getName( pattern , archetype ) :

    # Discard archetype for now
    name = ""

    for x in list(pattern) : 
	
        if ( str(x) == "c" ) : 
          name += str(pickOne(consonants))
        else :
          name += str(pickOne(vowel))

    return name[0:1].upper() + name[1:] 


for x in range(0,100) :

    pattern = random.randint(0,5)

    if ( pattern == 0 ):
      print str(x) + ":  " + getName("cvcv","none")
    elif ( pattern == 1 ):
      print str(x) + ":  " + getName("cvcvc","none")
    elif ( pattern == 2 ):
      print str(x) + ":  " + getName("cvc","none")
    elif ( pattern == 3 ):
      print str(x) + ":  " + getName("cvvc","none")
    elif ( pattern == 4 ):
      print str(x) + ":  " + getName("ccvc","none")
    elif ( pattern == 0 ):
      print str(x) + ":  " + getName("cvv","none")
    else :
      print str(x) + ":  " + getName("vvcvc","none")