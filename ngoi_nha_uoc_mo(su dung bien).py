import turtle
import math
turtle.bgcolor("cadetblue1")
turtle.speed(10)
canh_mai = 100*math.sqrt(2)
canh_dai = 200

#vẽ ngôi nhà
turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
i=0
while (i<4):
    turtle.forward(canh_dai)
    turtle.left(90)
    i = i + 1
turtle.end_fill()
turtle.left(90)
turtle.forward(canh_dai)

#vẽ mái

turtle.fillcolor("deeppink1")
turtle.begin_fill()
turtle.right(45)
turtle.forward(canh_mai)
turtle.right(90)
turtle.forward(canh_mai)
turtle.end_fill()

#vẽ cạnh mái
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.left(90)
turtle.forward(canh_mai)
turtle.left(90)
turtle.forward(canh_mai)
turtle.left(90)
turtle.forward(canh_mai)
turtle.left(90)
turtle.forward(canh_mai)
turtle.end_fill()

#vẽ nốt
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.left(90)
turtle.forward(canh_mai)
turtle.right(135)
turtle.forward(canh_dai)
turtle.right(45)
turtle.forward(canh_mai)
turtle.end_fill()

#vẽ cửa
chieu_dai_cua = 100
chieu_rong_cua = 75
turtle.fillcolor("palegreen1")
turtle.begin_fill()
turtle.right(45)
turtle.forward(chieu_rong_cua)
turtle.right(90)
turtle.forward(chieu_dai_cua)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(chieu_dai_cua)
turtle.end_fill()

#ve cua so
turtle.penup()
turtle.goto(-55,-140)
turtle.pendown()
canh_cua_so = 30

turtle.fillcolor("brown")
turtle.begin_fill()
turtle.forward(canh_cua_so)
turtle.left(135)
turtle.forward(canh_cua_so)
turtle.left(45)
turtle.forward(canh_cua_so)
turtle.left(135)
turtle.forward(canh_cua_so)
turtle.left(45)
turtle.end_fill()

#vẽ thân cây
turtle.penup()
turtle.goto(150,-300)
turtle.pendown()

turtle.fillcolor("brown")
turtle.begin_fill()
turtle.backward(90)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(40)
turtle.end_fill()

#vẽ tam giác cây
canh_cay_thong1 = 160
turtle.fillcolor("palegreen2")
turtle.begin_fill()
turtle.penup()
turtle.goto(90,-210)
turtle.pendown()
turtle.backward(canh_cay_thong1)
turtle.left(120)
turtle.backward(canh_cay_thong1)
turtle.left(120)
turtle.backward(canh_cay_thong1)
turtle.end_fill()

canh_cay_thong2 = 140
turtle.fillcolor("palegreen2")
turtle.begin_fill()
turtle.penup()
turtle.goto(100,-210+math.sqrt(160**2-80**2))
turtle.pendown()
turtle.forward(canh_cay_thong2)
turtle.right(120)
turtle.forward(canh_cay_thong2)
turtle.right(120)
turtle.forward(canh_cay_thong2)
turtle.end_fill()

canh_cay_thong3 = 100
turtle.fillcolor("palegreen2")
turtle.begin_fill()
turtle.penup()
turtle.goto(120,-210+math.sqrt(160**2-80**2)+math.sqrt(140**2-70**2))
turtle.pendown()
turtle.backward(canh_cay_thong3)
turtle.left(120)
turtle.backward(canh_cay_thong3)
turtle.right(60)
turtle.forward(canh_cay_thong3)
turtle.end_fill()

#Vẽ mặt trời
turtle.penup()
turtle.goto(200,350)
turtle.pendown()
turtle.goto(200,150)

turtle.penup()
turtle.goto(100,250)
turtle.pendown()
turtle.goto(300,250)

turtle.penup()
turtle.goto(125,325)
turtle.pendown()
turtle.goto(275,175)

turtle.penup()
turtle.goto(275,325)
turtle.pendown()
turtle.goto(135,185)

turtle.penup()
turtle.goto(160,280)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()


turtle.done()