from turtle import Screen, Turtle
import time

window = Screen()
window.title("7 Points Star")

pen = Turtle()
pen.pensize(4)

for i in range(7):
    pen.left(51.428)            # internal angle of rotation is 51.428 as in every isosceles triangle formed by the star, one angle is 77.143
    pen.forward(50)
    #time.sleep(1)
    pen.right(102.857)          # external angle of rotation is 102.857
    pen.forward(50)
    #time.sleep(1)

time.sleep(5)

#Note: internal angle = 77.143
# internal angle of rotation = 51.428 (i.e(2a = 180-77.143) thus a=51.428)
# external angle of rotation = 102.857 (i.e 180-77.143)
