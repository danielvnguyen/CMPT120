# Mind Reader Game
# Daniel Nguyen
# Sept 25th, 2020
# import replit #to clear the screen

# Introduce the game
print("Welcome to Mind Reader!")
words = ["cat", "dog", "apple"]

# TODO: Initialize score
score = 0 


for word in words:

  # Ask player 1 to enter 3 words
  print("Player 1, enter 3 words you think of when I say " + word)

  # Get the 3 words
  first = input("First word: ")
  second = input("Second word: ")
  third = input("Third word: ")

  # Ask Player 2 for their guess
  print("Player 2, what is one word you think Player 1 associates with " + word)
  guess = input()

  # Check if they win
  if guess in [first, second, third]:
    print("You've got it!")

    # TODO: Add to their running score
    score = score + 1 #can also do score += 1
  else: 
    print("No match!")
  
# TODO: At the end, print out their score
print("You got " + str(score) + " points!") #at end of 3 rounds
