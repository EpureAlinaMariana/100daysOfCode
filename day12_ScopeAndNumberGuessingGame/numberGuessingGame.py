#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import logo

#logo created with the link below
#http://patorjk.com/software/taag/#p=display&h=2&v=1&f=X992&t=guess
#debug editor can be find in the link below
#https://pythontutor.com/render.html#mode=display
print(logo)

#define CONSTANTS as a global variables to call and acces inside functions
TRIALS_EASY_LEVEL = 10
TRIALS_HARD_LEVEL = 5

def difficulty():
  """set the number of trials available in order to set difficulty of the game"""
  dificultyType = input("Chose a difficulty. Type 'easy' or 'hard': ")
  
  if dificultyType =="easy":
    return TRIALS_EASY_LEVEL
    print (f"You have {TRIALS_EASY_LEVEL} attempts remaining to guess the number.")
  elif(dificultyType == "hard"):
    return TRIALS_HARD_LEVEL
    print (f"You have {TRIALS_HARD_LEVEL} attempts remaining to guess the number.")
  else:
    print ("Invalid choice.")

def checkAnswer(rndNrToGuess, trial,trials):
  """check the given answer"""
  difference  = rndNrToGuess - trial
  
  if(difference <0 and abs(difference) <= 5):
    print("just a hint...you are closly but your number is too high.\n Try again with a slightly smaller number.")
    
  elif(difference >0 and difference <= 5):
    print("just a hint...you are closly but your number is too low.\n Try again with a slightly bigger number.")
    
  elif(trial > rndNrToGuess ):
    print("Too high.\nGuess again.")
   
  elif(trial < rndNrToGuess):
    print("Too low.\nGuess again.")
    
  elif(trial == rndNrToGuess):
    print("Congrats...you guess the number!!")

  else:
    print ("You inserted a wrong number...please try again!")
  return trials-1  
  



def guess_game():
  """complete steps for game"""
  guess =0
  numberOfTrials = difficulty()
  while(guess != numberToGuess):
    guess = int(input("Make a guess: "))
    numberOfTrials = checkAnswer(numberToGuess,guess,trials = numberOfTrials)
    print (f"You have {numberOfTrials} attempts remaining to guess the number.")
    if(numberOfTrials ==0):
      print("Game over!!! No trials available!")
      return


#start the game and generate a random int to be guess by the player
print ("Welcome to the Number Guessing Game")
print("I am thinking to a number between 1 and 100")
numberToGuess = random.randint(1,100)
print(numberToGuess)      
guess_game()