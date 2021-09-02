# Chatbot that loops until you give it valid input
# Daniel Nguyen
# October 19th, 2020

# Boolean control variable
valid_input = False

# Keep looping as long as the input isn't valid
while not valid_input:

  # Get input format
  answer = input("Do you like chicken? (Y/N): ").lower()

  # Update the control variable
  if answer == "yes" or answer == "y":
    print("Me too!")
    valid_input = True
  elif answer == "no" or answer == "n":
    print("Hmm!")
    valid_input = True
  else:
    print("Please type Yes or No!")
