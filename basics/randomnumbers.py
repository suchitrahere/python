import random
# function to generate 20 random integers 
def generaterandomintnumber(x, y):
    for i in range(20):
      print(random.randint(x, y))

def generaterandomfloatnumber(x, y):
    for i in range(20):
      print(random.ranndom(x, y))

def generaterandomuniquenumber(x, y):
    for i in range(20):
      print(random.unique(x, y))

def generaterandomfromlist():
    colors = ['red','black','green']
    for i in range(10):
      print(random.choice(colors))

#The function when called, we need to specify the range of random numbers to generate. Below one, I am generating random numbers in the range
#of 1 and 1000
generaterandomintnumber(1,1000)

#below function generates a list of random colors from the list
generaterandomfromlist()