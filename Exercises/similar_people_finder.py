# Similar People Finder
# Daniel Nguyen
# Oct. 9, 2020

# 1. Open the file
file = open("favourites-survey-fall2020.csv")
junk_header = file.readline()

# 2. Read the first line and get my list of favourite things
my_favourites = file.readline().strip().split(",")[3:8]

# 3. Initialze variables
top_friend = ""
top_score = 0 
top_friends = []

# Go through all people in the file
for line in file:

  # Get their name and list of favourites
  person_data = line.strip().split(",")
  their_name = person_data[1]
  their_favourites = person_data[3:8]

  # Calculate their similarity score
  common_interest_tally = 0 
  for favourite in my_favourites:
    if favourite in their_favourites:
      common_interest_tally += 1 
      
  # If their score is higher than the current top score
  # set the top friend name to that 
  if common_interest_tally >= top_score: #last person in the list
    top_friend = their_name
    top_score = common_interest_tally

  # If their similarity score was also high,
  # add to top friends list
  if common_interest_tally > 2:
    top_friends = top_friends + [their_name]

# Print top friend and top friends list
print(top_friend, "with score", top_score)
print(top_friends)
