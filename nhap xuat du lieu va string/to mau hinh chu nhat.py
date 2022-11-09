import turtle
import math
color = input("Nhập màu cần tô: ")
chieu_dai = float(input("Nhập vào chiều dài: "))
chieu_rong = float(input("Nhập vào chiều rộng:"))

t = turtle.Turtle()
t.hideturtle()
t.color(color)
t.begin_fill()

i = 0
while i < 2:
    t.forward(chieu_dai)
    t.right(90)
    t.forward(chieu_rong)
    t.right(90)
    i = i + 1
t.end_fill()
turtle.done()

c = 2 * (chieu_dai + chieu_rong)
s = chieu_dai * chieu_rong

print("Chu vi hình chữ nhật (dài = {w}, rộng = {h}) là {c}".format(w = chieu_dai, h = chieu_rong, c = c))
print("Diện tích hình chữ nhật (dài = {w}, rộng = {h} là {s}".format(w = chieu_dai, h = chieu_rong, s = s))
