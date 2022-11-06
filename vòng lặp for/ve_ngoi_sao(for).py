import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star")

turtle.speed(0)
turtle.pencolor("red")
for i in range(1, 100):
    for j in range(1,6):
        turtle.left(144)
        turtle.forward(200)
    turtle.left(5)
    
turtle.done()
