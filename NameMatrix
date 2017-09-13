import random

letters = (" ","a","b","c","d","e","f","g","h","i","j","k","l","m",
           "n","o","p","q","r","s","t","u","v","w","x","y","z")

matrix = [[ 1 for x in range(len(letters)) ] for y in range(len(letters)) ]


#
# prints matrix
def out():
  
  for x in range(0, len(matrix) ):
    print "--- " + letters[x] + " ---"

    for y in range( 0, len(matrix[x]) ):
      print (matrix[x])[y]
 
#
# Makes a word of length length
def create( length ):

  word = ""
  total = 0
  
  # Create first chear
  word += letters[select( matrix[0] )]
  
  last_char = word
  
  
  for x in range(length):
  
    word += letters[select(matrix[letters.index(last_char)])]
    
    last_char =  word[-1]
    
  return word
    

# selects item from weighted list
def select( letter_weights ):    
  
  #print letter_weights
  
  total = 0
  
  for x in range(len(letter_weights)):
    total += letter_weights[x]
  
  selected = random.randint( 1, len(letter_weights) - 1)
  
  while True:
    if random.randint(0,total) < letter_weights[selected] :
      return selected # return index of letter
    else :
      selected = random.randint(0, len(letter_weights) - 1)

# Breaks data into trainable pairs
def train_set( data ):
  
  for x in range( len(data) - 1 ):
    
    # Train space before word
    #matrix[0][letters.index(list(data[0]))] += 1
    
    for y in range( len(list(data[x])) - 1):
      
      matrix[letters.index( list(data[x])[y])][letters.index( list(data[x])[y + 1] )] += 1
  

train_set( ["john", "mark" , "phil", "austin", "tom" , "jim", "tony", "sam", "steve" ] )

for x in range(10):
  print str(x + 1) + ": " + str(create( 5 ))
