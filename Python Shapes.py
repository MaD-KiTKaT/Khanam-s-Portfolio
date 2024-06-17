import turtle
import random

# Create turtle object
t = turtle.Turtle()

# Draw a big circle
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
# Move to a new position
t.penup()
t.goto(50, 100)
t.pendown()
# Draw a small circle
t.fillcolor("white")
t.begin_fill()
t.circle(20)
t.end_fill()

# Turn turtle
t.left(180)
# Move to a new position
t.penup()
t.goto(-50, 130)  
t.pendown()
# Draw another small circle
t.fillcolor("white")
t.begin_fill()
t.circle(20)
t.end_fill()
#---------------------------------
t.left(90)
t.penup()
t.goto(60, 80)
t.pendown()

t.fillcolor("pink")
t.begin_fill()
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(115)
t.end_fill()

col = ["red","blue","green","purple"]
def square():
    t.fillcolor(random.choice(col))
    t.begin_fill()
    for i in range(4):
        t.forward(10)
        t.right(90)
    t.end_fill()
 
t.left(135)
t.penup()
t.goto(0, 85)
t.pendown()
square()


# Close the turtle graphics window
turtle.done()
