import random

print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 

target = random.randint(1,101)

def take_guess():
  guess = int(input('Please enter a guess between 1 and 100'))
  if guess == target:
    print(f'You win!  You guessed {guess} and the answer was {target}! Kudos!')
  elif guess > target:
    print(f'{guess} is too high.  Guess a lower number.')
    take_guess()
  elif guess < target:
    print(f'{guess} is too low.  Guess a higher number.')
    take_guess()

take_guess()