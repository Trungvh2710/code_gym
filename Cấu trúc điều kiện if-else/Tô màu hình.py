import turtle
import random

number = random.uniform(0, 3)
intnumber = int(number)
turtle.bgcolor("blue")
turtle.shape("circle")

if intnumber < 1:
    turtle.color("green")
elif intnumber < 2:
    turtle.color("yellow")
elif intnumber < 3:
    turtle.color("red")

turtle.done()