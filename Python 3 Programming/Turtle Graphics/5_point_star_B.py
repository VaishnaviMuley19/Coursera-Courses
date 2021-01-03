from turtle import Screen, Turtle
import time

window = Screen()
window.title("5 Points Star")
pen = Turtle()
pen.pensize(4)

pen.left(72)                # rotates the turtle in left direction by 72 degrees
pen.forward(200)

#time.sleep(1)

for i in range(4):
    pen.right(144)          # as each internal angle of the 5 point star is of 36 degrees and external is 144
    pen.forward(200)
    #time.sleep(1)

time.sleep(5)

#Note: internal angle = 36
# internal angle of rotation = 72 (as an isosceles triangle is formed by the stars whose one angle connecting the two equal sides is 36)
# external angle of rotation = 144 (i.e 180-36)
