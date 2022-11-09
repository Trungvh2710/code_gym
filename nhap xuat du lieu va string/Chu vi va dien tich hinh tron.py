import turtle
import math
r = int(input("Nhập vào bán kính: "))
t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.color("red")
t.circle(r)

c = 2 * math.pi * r
s = math.pi * r**2
print("Chu vi của hình tròn có bán kính = {r} là {c}".format(r=r, c=c))
print("Diện tích của hình tròn có bán kính = {r} là {s}".format(r=r, s=s))
turtle.done()