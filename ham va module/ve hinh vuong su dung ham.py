import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor("red")

def draw_square(w):
    for i in range(4):
        t.forward(w)
        t.right(90)
    turtle.done()
draw_square(100)