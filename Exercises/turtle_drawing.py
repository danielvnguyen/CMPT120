# Turtle Drawing
# Daniel Nguyen
# Oct 14th, 2020

# Import turtle module
import turtle

# Create a turtle 
anna = turtle.Turtle()

for i in range(20):

  # Stamp
  anna.stamp()

  # Move forward 10 pixels
  anna.forward(10)

  # Clearing
  anna.clear()

  # More ways to Animate
  anna.right(180)
  anna.penup() # gets rid of pen trail
  anna.forward(200)
