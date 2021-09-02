# Practice Quiz Q7
# Daniel Nguyen
# November 6th 2020

import cmpt120image
beach = cmpt120image.getImage('beach.jpg')
#red = cmpt120image.getImage('red.jpg')

width = len(beach)
height = len(beach[0])

def isBlue(img,x,y):
  pixel = img[x][y]
  r = pixel[0]
  g = pixel[1]
  b = pixel[2]
  return b > 130

print(isBlue(beach,0,0))

# Loop through all the pixels 
for x in range(width):
  for y in range(height):
# If a pixel is green, set it to the beach image
    if isBlue(beach,x,y): #using our module
      beach[x][y] = [255,0,0]

# Save the image 
cmpt120image.saveImage(beach,"output.jpg") #creates output.jpg on the left
