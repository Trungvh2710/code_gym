import turtle
import math
def draw(r):
    t = turtle.Turtle()
    t.hideturtle()
    t.pencolor("red")
    t.circle(r)
    turtle.done()
def area(r):
    return math.pi*r*r
r = float(input("Nhập vào bán kính hình tròn: "))
draw(r)
s = area(r)
print("Diện tích hình tròn có bán kính = {} là: {}".format(r,s))