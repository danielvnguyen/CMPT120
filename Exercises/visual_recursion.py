# Visualizing Recursion
# Daniel Nguyen
# October 21st, 2020

import turtle
pete = turtle.Turtle()

# Recursive function
def vortex(size):
  # base case
  if size >= 10:
    #pete.dot(5)
 # else:
    # call myself
    pete.circle(size)
    vortex(size*0.75)

vortex(100)
