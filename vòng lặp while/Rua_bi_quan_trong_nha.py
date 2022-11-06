import turtle
import random
turtle.penup()
turtle.goto(0, -200)

turtle.speed(10)
turtle.pensize(10)
turtle.pencolor("black")
turtle.pendown()
turtle.circle(200)

turtle.penup()
turtle.goto(0, 0)
turtle.shape("turtle")
turtle.pencolor("green")

angle = random.randint(0, 360)
turtle.right(angle)
cnt = 0
while True:
    turtle.speed(1)
    turtle.forward(185)
    turtle.speed(10)
    turtle.goto(0, 0)
    angle = random.randint(0, 360)
    turtle.right(angle)
    cnt = cnt + 1
    if cnt == 15:
        break

turtle.done()
