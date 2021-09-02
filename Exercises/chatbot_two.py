# Title: How's It Going Bot
# Author: Daniel Nguyen
# Date: September 16th, 2020

# Description: This bot will ask you how it's going and make a comment depending on how you replied.

# Ask user how it's going
print ("Hi! How's it going?")

# Get the user's reply and store it in a variable
reply = input()

# If they said Good, then reply Great!
if reply  == "Good" or reply == "good":
  print("Great!")

# Otherwise, if they said Bad, then reply Oh no!
elif reply == "Bad" or reply == "bad":
  print ("Oh no!")
  print ("That's too bad.")

elif reply == "Amazing":
  print ("That's awesome!")

# Otherwise, in all other case reply "I see.."
else:
  print ("Oh, alright.")
