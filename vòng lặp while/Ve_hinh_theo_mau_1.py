import turtle
r = int(input("Nhập bán kính: "))
turtle.penup()
turtle.goto(-50,-50)
turtle.pendown()
turtle.seth(-45)
for i in range(2):
    turtle.circle(r,90)
    turtle.circle(r/2,90)

turtle.done()