# SFU Popular Cafes
# Author: Daniel Nguyen
# Date: Sept. 28, 2020
# Ask 5 people their favourite SFU cafe and output the number of people who like Starbucks, Renaissance or Tim Hortons

# Initialize tallies
starbucks_tally = 0
renaissance_tally  = 0
tims_tally = 0

# can also use range as range(10,0,-1), where 10 is start, 0 is end, -1 is the increments. in this case going backwards.
for i in range(5):
  # Ask the person what their favourite cafe is
  fave_cafe = input("What is your favourite cafe? ").lower()

  # If they say starbucks, add one to the Starbucks tally 
  if fave_cafe == "starbucks":
    starbucks_tally += 1

  # If they say Renaissance, add one to the Renaissance tally
  elif fave_cafe == "renaissance":
    renaissance_tally += 1

  # If they say Timmy's, add one to the Tim Horton's tally
  elif "tim" in fave_cafe:
    tims_tally += 1

print("Starbucks: " + str(starbucks_tally/5*100) + "%") #convert tally to str to contatenate
print("Renaissance: " + str(renaissance_tally/5*100) + "%")
print("Tim Hortons: " + str(tims_tally/5*100) + "%")
