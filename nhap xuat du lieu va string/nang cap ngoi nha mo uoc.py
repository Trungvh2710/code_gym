import turtle
t = turtle.Turtle()

t.speed(10)
t.penup()
t.goto(-160,-160)
t.pendown()
t.pencolor("black")
t.pensize(1)
#vẽ ngôi nhà
t.fillcolor("yellow1")
t.begin_fill()
i = 0
while i < 2:
    t.forward(320)
    t.left(90)
    t.forward(200)
    t.left(90)
    i = i + 1
t.end_fill()

#vẽ cửa nhà
t.penup()
t.goto(-40,-160)
t.pendown()
t.fillcolor("royalblue1")
t.begin_fill()
t.left(90)
t.forward(100)
t.right(90)
t.forward(80)
t.right(90)
t.forward(100)
t.end_fill()

#vẽ mái
t.penup()
t.goto(-160,40)
t.pendown()
t.fillcolor("firebrick1")
t.begin_fill()
t.goto(-60,140)
t.goto(40,40)
t.end_fill()

#vẽ ống khói
t.penup()
t.goto(-20,100)
t.pendown()
t.fillcolor("olive")
t.begin_fill()
t.goto(-20,140)
t.goto(0,140)
t.goto(0,80)
t.end_fill()

t.penup()
t.goto(-20,160)
t.pendown()
t.pensize(4)
t.pencolor("gray49")
t.backward(20)
t.penup()
t.goto(0,190)
t.pendown()
t.forward(40)

#vẽ cây bên trái
t.penup()
t.goto(-300,-240)
t.pendown()
t.pensize(1)
t.color("gray57")
t.begin_fill()
t.left(90)
t.forward(40)
t.goto(-270,-160)
t.backward(20)
t.goto(-300,-240)
t.end_fill()

t.penup()
t.goto(-330,-160)
t.pendown()
t.pencolor("chartreuse3")
t.color("darkgreen")
t.begin_fill()
t.goto(-230,-160)
t.goto(-280,-120)
t.goto(-330,-160)
t.end_fill()
t.penup()
t.goto(-320,-120)
t.pendown()
t.color("chartreuse3")
t.begin_fill()
t.goto(-240,-120)
t.goto(-280,-80)
t.goto(-320,-120)
t.end_fill()
t.penup()
t.goto(-300,-80)
t.pendown()
t.color("darkolivegreen2")
t.begin_fill()
t.goto(-260,-80)
t.goto(-280,-50)
t.goto(-300,-80)
t.end_fill()

#vẽ cây bên phải
t.penup()
t.goto(300,-240)
t.pendown()
t.pencolor("dodgerblue1")
t.color("gray57")
t.begin_fill()
t.goto(380,-240)
t.goto(360,-120)
t.goto(320,-120)
t.goto(300,-240)
t.end_fill()

t.penup()
t.goto(240,-120)
t.pendown()
t.pencolor("chartreuse3")
t.color("darkgreen")
t.begin_fill()
t.goto(440,-120)
t.goto(340,-40)
t.goto(240,-120)
t.end_fill()
t.penup()
t.goto(260,-40)
t.pendown()
t.color("chartreuse3")
t.begin_fill()
t.goto(420,-40)
t.goto(340,20)
t.goto(260,-40)
t.end_fill()
t.penup()
t.goto(290,20)
t.pendown()
t.color("darkolivegreen2")
t.begin_fill()
t.goto(390,20)
t.goto(340,80)
t.goto(290,20)
t.end_fill()

turtle.done()








