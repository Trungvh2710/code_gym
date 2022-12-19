import turtle
import math

class Circle:
    def __init__ (self, r, x, y):
        self.x = x
        self.y = y
        self.r = r
    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(self.r)
        turtle.done()
    def area(self):
        return math.pi * self.r**2
    def perimeter(self):
        return math.pi * 2 * self.r

c = Circle(100, -200, 0)
c.draw()
print("S = ", c.area())
print("C = ", c.perimeter())