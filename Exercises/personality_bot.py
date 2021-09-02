# Title: Chatbot with Personality Exercise
# Author: Daniel Nguyen
# Date: September 16th, 2020

# Description: Chatbot must ask at least 3 questions, must use if/elif/else 
# at least once, it must use an answer (input) from the user in its response, 
# and use the keyword 'or' to accept at least 2 forms of input from the user.

print ("Hello! My name is Chatbot. Do you like cats or dogs more? ")
reply = input().lower()

if reply == "Dogs" or reply == "dogs":
  print ("Great! What's your favourite kind of dog?")
  doggy = input()
  print (doggy + "'s are cute! I like corgis!")

elif reply == "Cats" or reply == "cats":
  print ("Cats are cool. What's your favourite colour cat?")
  kitty = input()
  print ("I like " + kitty + " cats too!")

else:
  print ("Pardon me?")
