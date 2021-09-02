# Draw A Cookie
# Daniel Nguyen
# Oct 15th, 20200

# Make the turtle
import turtle
anna = turtle.Turtle()

#COOKIE FUNCTION
def draw_cookie(x,y): #with an input of coordinates
# Draw the outside of the cookie
  anna.penup()
  anna.goto(-5+x,-30+y)
  anna.pendown()
  anna.circle(30)

  # Chocolate chips
  anna.penup()
  anna.goto(0+x,0+y)
  anna.stamp() #stamp STAMPS the turtle
  anna.goto(-10+x,10+y)
  anna.stamp()
  anna.goto(10+x,-10+y)
  anna.stamp()
  anna.goto(-10+x,-10+y)
  anna.stamp()
  anna.goto(10+x,10+y)
  anna.stamp()

draw_cookie(7,69) #uses function
draw_cookie(-100,-20)
