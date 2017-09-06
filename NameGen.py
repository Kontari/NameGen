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
               letter("q",1), letter("r",12), letter("s",13), letter("t",13),
               letter("v",2), letter("w",4), letter("x",1), letter("y",4),
               letter("z",1) ]

extended = consonants + [ letter("ph", 6), letter("tt", 6), letter("th", 6),
                          letter("er", 6), letter("ing", 6), letter("ph", 6),
                          letter("li", 6), letter("el", 6), letter("ic", 6)]

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

    while True:
      randSelect = random.randint(0 , len(options) - 1)

      if ( random.randint(0, totalWeight) < options[randSelect].weight ):
        return options[randSelect].out


# Takes in a string of cv's
def getName( pattern , archetype ) :

    # Discard archetype for now
    name = ""

    for x in list(pattern) : 
	
        if ( str(x) == "c" ) : 
          name += str(pickOne(extended)) #consonants
        else :
          name += str(pickOne(vowel))

    return name[0:1].upper() + name[1:] 

syl = ["cv","cvc","vc","c","v"]

for x in range(0,10) :

    name = ""

    syls = random.randint(2,5)

    y = 0 
    
    # MinLen + MaxLen
    while y < syls and (len(name) >= 8 or len(name) <= 3) :
      name += syl[random.randint(0,len(syl) - 1)]
    
    '''
    Gateway requirements

    Ro3
    MinLen
    MaxLen
    Entropy (length of c/v chains)
    Repeats
    '''
    
    # Ro3 + Entropy
    name = name.replace("ccc", syl[random.randint(0,len(syl) - 1)])




    print str(x + 1) + ": " + getName( name , "" )


