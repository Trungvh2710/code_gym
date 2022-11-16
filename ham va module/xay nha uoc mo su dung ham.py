import turtle
t = turtle.Turtle()
t.speed(10)
t.pencolor("blue")

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

def draw_polygon(toa_do, n, canh = 100, mau = "white"):
    t.penup()
    t.goto(toa_do)
    t.pendown()
    t.fillcolor(mau)
    t.begin_fill()
    angle = (n-2)*180/n
    for i in range(n):
        t.forward(canh)
        t.left(180-angle)
    t.end_fill()
    
#vẽ ngôi nhà
draw_rectangle((-160,40), 320, 200, "white")
draw_rectangle((-40,-60), 80, 100, "white")
draw_rectangle((-20,160), 20, 120, "white")
draw_polygon((-160,40), 3, 200, "white")
t.penup()
t.goto(-20,180)
t.pendown()
t.right(90)
t.backward(20)
t.penup()
t.goto(0,210)
t.pendown()
t.forward(40)

#vẽ cây bên trái
t.penup()
t.goto(-300,-240)
t.pendown()
t.color("gray57")
t.begin_fill()
t.left(90)
t.forward(40)
t.goto(-270,-160)
t.backward(20)
t.goto(-300,-240)
t.end_fill()
draw_polygon((-330,-160),3,100, "darkgreen")
draw_polygon((-320,-90),3,80, "chartreuse3")
draw_polygon((-300,-20),3,40, "darkolivegreen2")

#vẽ cây bên phải
t.penup()
t.goto(300,-240)
t.pendown()
t.color("gray57")
t.begin_fill()
t.goto(380,-240)
t.goto(360,-120)
t.goto(320,-120)
t.goto(300,-240)
t.end_fill()
draw_polygon((260,-120),3,160, "darkgreen")
draw_polygon((280,20),3,120, "chartreuse3")
draw_polygon((300,120),3,80, "darkolivegreen2")

turtle.done()