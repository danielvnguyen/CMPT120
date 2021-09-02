 # Chip Rater
 # Daniel Nguyen
 # Sept 30th, 2020

 # Greetings
print("Welcome to Chip Rater. I will ask you a few questions!")

 # Make a list of questions 
questions = ["How crispy is the chip out of 5? ", "How would you rate the taste out of 5? ", "Out of 5, how would you rate the packaging? "]

# Initialize the score
score = 0

 # Go through each question question and get a rating.
for question in questions:
  rating = int(input(question))
  score += rating

 # Calculate the final score.
print("Rating: " + str(score/len(questions)) + "/5.0")
