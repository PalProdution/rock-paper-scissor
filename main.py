import random #importing the random module
 
#initializing the variables
choices = ('r', 'p', 's')
cPoints = 0
pPoints = 0
 
def player():
   
  '''This function is used to get players choice.'''
   
  global choices #declaring the variable choices to be global
  symbol = input("Choose either rock(r), paper(p), or scissors(s). ").lower()
   
   
  if symbol not in choices:
    print("You did not enter a valid option. ")
    return player() #using recursion to get a valid input
  else:
    return symbol#if valid input return the answer
 
def computer():
 
  '''This function is used to get computers choice'''\
   
  return random.choice(choices)
 
def game():
 
  '''This function is used to play a single round of game'''
   
  global cPoints, pPoints #declaring cPoints and pPoints to be global
  pChoice = player()#getting the players choice
  cChoice = computer()#getting the computers choice
  print("The computer has chosen", cChoice)
  print("You chose", pChoice)
  if pChoice == cChoice: #checking for tie
    print("Its a tie! No one gets a point. ")
  elif (pChoice == "r" and cChoice == "s") or (pChoice == "s" and cChoice == "p") or (pChoice == "p" and cChoice == "r"): #checking if player scores a point
