import turtle
shapeInput = input("Circle, square or turtle, Nhập vào hình dáng con trỏ?")
colorInput = input("red, yellow or blue, Nhập vào màu con trỏ?")
turtle.bgcolor("green")
turtle.title("Thay đổi con trỏ chuột")

if shapeInput == "circle" or shapeInput == "square" or shapeInput == "turtle":
    turtle.shape(shapeInput)
    if colorInput == "red" or colorInput == "yellow" or colorInput == "blue":
        turtle.color(colorInput)
    else:
        print("Màu nhập vào không đúng")
else:
    print("Hình dáng con trỏ không hợp lệ")

turtle.done()