### Part Two -- your code goes here. 
import random                                                 # imports random library
randNum = random.randint(0, 100)                               # makes a random number equal 'randNum' in a range from 0 - 100
userGuess = int(input("Guess a number between 1 - 100: "))      # asks the user to make a guess and assigns the integer to 'userGuess'
while userGuess != randNum:                                   # while the guess is false;
 userGuess = int(input("Try guess again: "))                   # userGuess gets reassigned to the users new guess
 if userGuess == randNum:                                    # when the user guesses right;
   print("Congratultions you da best at guessing stuff yo")   # program will print a string saying you win 