import turtle as t 
import random

screen = t.Screen()
screen.setup(height = 500, width = 600)
guess = screen.textinput(prompt="Du doan con rua nao win?", title = "Nhap vao mau con rua (do, nau, xanh duong, xanh la cay, cam, hong)? ")
colors = ["red", "brown", "blue", "green", "orange", "pink"]

# Vị trí ban đầu theo trục y của các con rùa
# Theo trục x = -250, cách vị trí 0,0 250 về bên trái
y_position = [0, -30, 30, -60, 60, 90]
turtle_speed = [10, 15, 20, 25, 30, 5]

all_turtles = []
run = True

for i in range(0, 6):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    # Di chuyển rùa về vị trí ban đầu,
    # bên trái cùng của đường đua
    turtles.goto(x=-250, y=y_position[i])
    # Màu của rùa
    turtles.color(colors[i])
    # Lưu vào list
    all_turtles.append(turtles)


def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.choice(turtle_speed))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 250:
            run = False

while run:
    random_walk(all_turtles)
    
screen.exitonclick()

