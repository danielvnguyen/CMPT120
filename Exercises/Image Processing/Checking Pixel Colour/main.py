# Checking pixel colour
# Daniel Nguyen
# November 2nd, 2020

import cmpt120image

def isGreen(r,g,b):
  '''
  r,g,b are integers between 0 and 255 inclusive
  Returns True if green, False otherwise.
  '''
  if r < 30 and 245 < g and b < 30:
    return True
  else:
    return False

img = cmpt120image.getImage('kid-green.jpg')
pixel = img[0][0]
print(isGreen(0,255,0))
