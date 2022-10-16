import turtle
cnt = 1
while (cnt <=5):
    turtle.forward(50)
    turtle.right(144)
    cnt = cnt + 1
    
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
    
cnt_hcn = 1
while (cnt_hcn < 5):
    turtle.forward(50)
    turtle.right(90)
    cnt_hcn = cnt_hcn + 1
    
turtle.circle(100)
turtle.done()