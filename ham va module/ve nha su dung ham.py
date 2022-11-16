import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor("blue")
t.speed(100)

def draw_rectangle(toa_do, canh_ngang, canh_doc, mau):
    t.penup()
    t.goto(toa_do)
    t.pendown()
    t.fillcolor(mau)
    t.begin_fill()
    for i in range(2):
        t.forward(canh_ngang)
        t.right(90)
        t.forward(canh_doc)
        t.right(90)
    t.end_fill()

#vẽ ngôi nhà bên trái
draw_rectangle((-90,150), 90, 150, "indianred3")
draw_rectangle((-60,100), 30, 50, "white")

draw_rectangle((0,150), 90, 150, "indianred3")
draw_rectangle((30,100), 30, 50, "white")

draw_rectangle((-90,0), 90, 150, "indianred3")
draw_rectangle((-60,-50), 30, 50, "white")

draw_rectangle((0,0), 90, 150, "indianred3")
draw_rectangle((30,-50), 30, 50, "white")

#vẽ ngôi nhà to bên phải
draw_rectangle((90,0), 180, 150, "gray74")

#vẽ cửa chính cho ngôi nhà bên phải
draw_rectangle((150,-75), 30, 75, "cadetblue4")
draw_rectangle((180,-75), 30, 75, "cadetblue4")


turtle.done()


