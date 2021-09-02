# Combining Images
# Daniel Nguyen
# November 4th, 2020

import cmpt120image
import greenchecker #import our greenchecker module

def isGreen(img,x,y): #testing is that one pixel is green
  ''' Parameters/Input: img - list of lists of RGB values
                        x - column location (x coordinate)
                        y - row location (y coordinate)
      Output: Returns True if green, False otherwise
  '''
  pixel = img[x][y]
  r = pixel[0]
  g = pixel[1]
  b = pixel[2]
  return r < 70 and 245 < g and b < 30

img = cmpt120image.getImage('kid-green.jpg')

print(isGreen(img,0,0))

# Open up green image
green = cmpt120image.getImage('kid-green.jpg')

# Open up beach image
beach = cmpt120image.getImage('beach.jpg')

# Open an image to draw to
final = cmpt120image.getImage('kid-green.jpg')

# Get the width and height of the images
width = len(green) # number of columns
height = len(green[0]) #height of one of those columns
print(width,height)

# Loop through all the pixels 
for x in range(width):
  for y in range(height):
# If a pixel is green, set it to the beach image
    if greenchecker.isGreen(green,x,y): #using our module
      final[x][y] = beach[x][y]

# Save the image 
cmpt120image.saveImage(final,"output.jpg") #creates output.jpg on the left
