# Greetings Chatbot
# Author: Daniel Nguyen
# Date: Sept 14, 2020
import random
import time

# Steps: Say hi, what is your name?
print ("Hello! My name is ChatBot. What is your name?")

# Get the user's name (input)
name = input()

# Respond with nice to meet you, <input>.
time.sleep(1)
print ("Very nice to meet you, " + name + "!" )

# Ask what your favourite book is
print ("What is your favourite book, " + name + "?")

# Let the user respond
book = input ()

# Then make a non-repetitive comment about it
# print ("I think " + book + " is a great book too!")

# Make a list of possible comments 
replies = [("I think " + book + " is a great book too!"),(book + " is a very popular book!"), ("Man, I'm tired of " + book + ".")]

# Choose one randomly from the list
random_comment = random.choice(replies)

# Say that random comment
time.sleep(1)
print (random_comment)
