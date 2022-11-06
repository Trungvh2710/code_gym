import turtle
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor('black')
color=['violet','blue','green','yellow','orange','red']

r = int(input("Nhập bán kính: "))
a = 10
b = 0
turtle.speed(100)
for i in range(36):
    turtle.seth(-a)
    turtle.pencolor(color[b])
     
    # to access different color
    if b==5:
        b=0
    else:
        b = b + 1
    for i in range(2):
        turtle.circle(r,90)
        turtle.circle(r//2,90)
    a = a + 10

turtle.done()
