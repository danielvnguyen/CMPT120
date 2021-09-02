# Number Guessing Game
# Daniel Nguyen
# October 19th, 2020 

import random

random_number = random.choice(range(0,101))

user_guess = int(input("What number would you like to guess?: "))

guessed_correctly = False
guesses_left = 8

while user_guess != random_number and guesses_left > 0:
  if user_guess > random_number:
    print("Lower!")
    user_guess = int(input("Guess another number!: "))
    guesses_left -= 1
  elif user_guess < random_number:
    print("Higher!")
    user_guess = int(input("Guess another number!: "))
    guesses_left -= 1
  elif user_guess == random_number:
    print("You guessed correctly!")
    guessed_correctly = True
