# Title: Chatbot with a Loop: Icecream Bot
# Author: Daniel Nguyen
# Date: Sept 25th, 2020

# Must use at least 2 string methods for robustness, the (in) keyword, and a for loop.
# You must also use a nested conditional (if/elif/else) at least once. (elif/else optional)
import random

flavours = ["banana", "strawberry", "blueberry"]

print("Greetings! I am the Icecream Bot. \nPlease answer me with [Yes/No]:")
reply = input("Do you enjoy icecream? ").lower().strip("!. ")

for flavour in flavours:
  if reply == "yes":
    print("Do you like " + flavour + " icecream?")
    preference = input().lower().strip("!. ")
    if preference == "yes":
      yes_responses = [("I love " + flavour + "!"), ("We have so much in common!"), (flavour + " is a great flavour!")]
      print(random.choice(yes_responses))
    elif preference == "no":
      no_responses = [("Oh.. Alright!"), ("You should really give " + flavour + " icecream a try!"), ("That's surprising!")]
      print(random.choice(no_responses))
    else:
      print("Uhh.. okay then.")
  elif reply == "no":
    print("Oh, that's too bad!")
    break
  else:
    print("Excuse me?")
    break
print("Welp, thanks for chatting with me!")
  
