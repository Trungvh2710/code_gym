import turtle as t
import random
screen = t.Screen()
screen.setup(height = 500, width = 600)
t.hideturtle()
t.penup()
t.speed(100)
t.goto(-250, 200)
for i in range(21):
    t.write(i)
    t.forward(25)

x = -250
t.goto(-250, 200)
t.right(90)
for i in range(21):
    for j in range(10):
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(10)
    t.penup()
    t.forward(5)
    t.write(i)
    t.goto(x + (i + 1) * 25, 200)

all_turtles = []
y_position = [160, 100, 40, -20]
colors = ['red', 'green', 'blue', 'black']
for turtle in range(0, 4):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    turtles.goto(x=-250, y=y_position[turtle])
    turtles.color(colors[turtle])
    for i in range(5):
        turtles.left(72)
    all_turtles.append(turtles)
    
def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 250:
            run = False
run = True
while run:
    random_walk(all_turtles)

screen.exitonclick()
