# City Bliss Evaluator
# Daniel Nguyen
# Sept 30th, 2020

# To help you figure out which city would fit you the best.

# Introduction
print("What city would you like to evaluate?")
city = input()
print("Okay, let's evaluate " + city + "!")

# Questions
questions = ["How would you rate the environment out of 5? ", "Rate the safety out of 5: ", "How would you rate the public transit out of 5? "]

# Initaliize score
weighted_average_score = 0

# Go through the questions 
for question in questions:
  # Get the score for each question
  rating = int(input(question))


  # Get a weight (<1.0) for how important the factor is - ex. "How important is that factor to you, out of 5?"
  weight = float(input("How important is this factor to you, out of 5? "))/5

  # Keep a running weighted score
  weighted_average_score += rating*weight

  # Calculate the average weighted score
print(weighted_average_score/len(questions))
