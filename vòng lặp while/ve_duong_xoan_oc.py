import turtle

x = int(input("Nhập khoảng cách so với tâm: "))
for i in range(x):
    turtle.forward(2+i/4)
    turtle.left(30-i/12)

turtle.done()