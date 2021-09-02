# Function File
# Daniel Nguyen
# November 8th, 2020
# Description: File with the 3 Manipulation Functions

# Import cmpt120imageWeek9 module to access getImage, etc.
import cmpt120imageWeek9 

def invert(pixels):
  '''
  Input: pixels - 2d array of RGB values
  Output: a new RGB array that is the inverted version of the original.
  '''
  # Create variables for the width and height of the image.
  width = len(pixels)
  height = len(pixels[0])
  # Create a blank image with the same dimensions to add the updated pixels to
  newimage = cmpt120imageWeek9.createBlackImage(width,height)
  # For each pixel
  for x in range(width):
    for y in range(height):
      # Create pixel variable with the pixel's RGB values.
      pixel = pixels[x][y]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      # Create the inverted RGB values by subtracting them from 255.
      inverted_red = 255 - r
      inverted_green = 255 - g
      inverted_blue = 255 - b
      # Update that pixel in 'newimage' with the inverted pixel.
      newimage[x][y] = (inverted_red, inverted_green, inverted_blue)
  return newimage

def cover(pixels):
  '''
  Input: pixels - 2d array of RGB values
  Output: a new RBG array that is the original but half of it is black.
  '''
  width = len(pixels)
  height = len(pixels[0])
  # For each pixel
  for x in range(width):
    for y in range(height):
      # If the pixel is in the bottom half of the image
      if y >= height//2:
        # Change that pixel to black
        pixels[x][y] = [0,0,0]
        newimage = pixels
  return newimage


def flipHorizontal(pixels):
  '''
  Input: pixels - 2d array of RGB values
  Output: a new RBG array that is the horizontally flipped version of the original.
  '''
  width = len(pixels)
  height = len(pixels[0])
  # Create a blank image with the same dimensions to add the updated pixels to
  newimage = cmpt120imageWeek9.createBlackImage(width,height)
  # For each pixel
  for x in range(width):
    for y in range(height):
      # Update that pixel in 'newimage' with the corresponding pixel on the opposite side.
      newimage[x][y] = pixels[width-1-x][y]
  return newimage
