import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor("red")

def draw(n, width=100):
    angle = (n - 2) * 180 / n
    for i in range(n):
        t.forward(width)
        t.right(180 - angle)
    turtle.done()
draw(6,150)