# Favourite Pets
# Daniel Nguyen
# October 5th, 2020
# Description: Find out if dogs or cats are more popular among CMPT120 students.

# Open the file
file = open("favourites-survey-fall2020.csv")

# Read the first line
questions = file.readline() # .readline() returns string for the current row
# discards that line from the file object

print(questions)

# Read the second line
# for i in range(): #this doesn't work b/c we don't know how many lines in the file
response = file.readline()
print(response)
