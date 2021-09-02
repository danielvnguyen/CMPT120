# Nosy Question Bot
# Daniel Nguyen
# Date: Sept. 25, 2020
# Description: Asks you a lot of questions

import random

# Introduction
print("Hello! This is Nosy Question Bot. I'd like to ask you some questions! Here we go.")

# Create questions list
questions = ["Given the choice of anyone in the world, who would you want to have dinner with?", "Would you like to be famous? Why?", "What would constitute a perfect day for you?", "Before making a phone call, do you ever rehearse what you're going to say?"]

# Make responses list
responses = ["I see!", "Interesting.", "Fascinating."]

# Make a loop that will ask questions from the questions list and, no matter the input from user, respond with a random answer from responses
for question in questions:
  print(question)
  reply = input()
  if "stop" in reply: #if user says "stop"
    break
  print(random.choice(responses))

print("Thanks for the chat!")
