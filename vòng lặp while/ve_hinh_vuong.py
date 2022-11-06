import turtle
x = int(input("Nhập độ dài các cạnh của hình vuông: "))
turtle.hideturtle()
turtle.pencolor("red")
i = 0
while i < 4:
    turtle.forward(x)
    turtle.right(90)
    i = i + 1

turtle.done()
