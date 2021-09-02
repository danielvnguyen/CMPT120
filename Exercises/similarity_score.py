# Comparing two people's favourite movies
# Author: Daniel Nguyen
# Date: Oct. 7, 2020

# Description: Finds out how similar two people are by 
# comparing their lists of favourite movies

# 1. Get the favourite movies for each person
angelica_favourite_movies = ["Big Hero 6", "Inside Out", "Wall-E"]
baymax_favourite_movies = ["Big Hero 6", "Star Wars", "Wall-E"]

# 2. Initialize a common interests counter
common_interests_counter = 0

# 3. Go through all the favourite movies of the first person
for movie in (angelica_favourite_movies):
  
  # 3a. If that movie is also in the 2nd person's list
   if movie in baymax_favourite_movies:
     common_interests_counter += 1
    
    # Add to the common interests counter

#4. Print the common interests counter to get a similarity score
print(common_interests_counter)
