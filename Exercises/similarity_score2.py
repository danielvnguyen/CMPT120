# Most Similar to Me
# Daniel Nguyen
# October 7th, 2020
# Description: Make an Advanced Recommendation System to find the people whose survey results are most similar to mine.
# Algorithm:
# 1. Compare yourself with one person at a time
# 2. Calculator your similarity score
# 3. Keep track of person most similar to you
# 4. Update top person w/ if someone is higher
# 5. At the end, you'll find the most similar person!


# Moved my results to first of file
# Open the file
file = open("favourites-survey-fall2020.csv")
file.readline() # Removes/process the header 
# Read the first line to get a list of my preferences
my_favourites = file.readline().strip().split(",")[1:] #splits all the elements in my results into a list, then gets rid of the date.

# Intialize variables for top friend and score
top_person = ""
top_score = 0

# Go through each line of the file
for line in file:
# Get their favourites/results
   person_data = line.strip().split(",")
   their_name = person_data[1]
   their_favourites = person_data[2:-1]

# Get similarity score:
# Initialize a common interest counter
common_interest_tally = 0
# For each of my favourite things, check if it is also in theirs.
for favourite in my_favourites:
  if favourite in their_favourites:
    common_interest_tally += 1

  # Check if their score is higher than the current top score
if common_interest_tally > top_score:
  # If so, set the highest scored name to them.
  top_person = their_name
  top_score = common_interest_tally

# Print the top person.
print(top_person, top_score)
