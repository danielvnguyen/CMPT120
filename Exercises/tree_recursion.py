# Drawing a Tree
# Daniel Nguyen
# October 21st, 2020

import turtle
bob = turtle.Turtle()

# Recursive function to draw tree
def draw_tree(level, branch_length):
  # Base case - leaf
  if level == 0: #BASE CASE
    bob.color("green")
    bob.stamp() # Draw a 'leaf'
    bob.color("brown")

  # Branch
  else:
    bob.forward(branch_length) # Draw branch

    # Turn left and make a mini-tree
    bob.left(40)
    draw_tree(level-1, branch_length/1.61)

    # Turn right and make another mini-tree
    bob.right(40)
    draw_tree(level-1, branch_length/1.61)

    # Turn right and make another mini-tree
    bob.right(40)
    draw_tree(level-1, branch_length/1.61)
    
    # Reset
    bob.left(40)
    bob.back(branch_length)

bob.left(90)
bob.speed(0)
bob.width(3)
bob.color("brown")
draw_tree(4, 100)
