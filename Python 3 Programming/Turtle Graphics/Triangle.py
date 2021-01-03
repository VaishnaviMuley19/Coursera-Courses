from turtle import Screen, Turtle
import time

window = Screen()
window.bgcolor("Pink")

pen = Turtle()
pen.pensize(4); pen.color("Purple")

for i in range(3):
    pen.forward(100)
    time.sleep(1)
    pen.left(120)                    #(180-60 = 120)

# As it ia an equilateral triangle, all the 3 internal angles of the triangle are of 60 degrees, thus external angle is 120 degrees.

