import turtle
import random
turtle.pensize(3)
turtle.color("blue")
turtle.speed(1)

turtle.penup()
turtle.goto(-400,0)

cnt = 0
while cnt < 10:
    down = random.randint(20, 40)
    up = random.randint(20,40)
    turtle.pendown()
    turtle.forward(down)
    turtle.penup()
    turtle.forward(up)
    cnt = cnt + 1

turtle.done()
