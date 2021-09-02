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
