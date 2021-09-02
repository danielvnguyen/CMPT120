# Interactive Image Processor
# Daniel Nguyen
# November 8th, 2020
# Description: Based on the users input, will either exit the program, show the
# original image, or manipulate the image by either inverting, covering, or 
# horizontally flipping it.

# Import the modules required for this program.
import cmpt120imageWeek9
import cmpt120imageManip

# Set the variable for the image we will be using
cat = cmpt120imageWeek9.getImage('week9-photo.jpg')

# Initialize control variable for the while loop
invalid_input = True

# While the user doesn't input a valid answer, keep looping.
while invalid_input:
  user_input = input("Hello! Please enter 0,1,2,3, or 4 to either: \n0: Exit the program \n1: See the original image \n2: Invert the image \n3: Change half of the image to black \n4: Horizontally flip the image \nChoose a number: ")

  # If the user enters 0, exit the program.
  if user_input == '0':
    # Update control variable
    invalid_input = False

  # If the user enters 1, show the original image.
  elif user_input == '1':
    invalid_input = False
    cmpt120imageWeek9.showImage(cat, 'Original Image')
    ok = input("Hit return to continue... ") 

  # If the user enters 2, show the inverted image.
  elif user_input == '2':
    invalid_input = False
    inverted_image = cmpt120imageManip.invert(cat)
    cmpt120imageWeek9.showImage(inverted_image, 'Inverted Image')
    ok = input("Hit return to continue... ") 

  # If the user enters 3, show the covered image.
  elif user_input == '3':
    invalid_input = False
    covered_image = cmpt120imageManip.cover(cat)
    cmpt120imageWeek9.showImage(covered_image, 'Covered Image')
    ok = input("Hit return to continue... ") 

  # If the user enters 4, show the horizonally flipped image.
  elif user_input == '4':
    invalid_input = False
    flipped_image = cmpt120imageManip.flipHorizontal(cat)
    cmpt120imageWeek9.showImage(flipped_image, 'Flipped Image')
    ok = input("Hit return to continue... ") 
    
  # Otherwise, if the input is invalid, keep looping.
  else:
    print("Sorry, I don't understand " + user_input)

