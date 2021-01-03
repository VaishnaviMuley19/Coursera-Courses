from turtle import Screen, Turtle
import time

window = Screen()
window.title("5 Points Star")
pen = Turtle()
pen.pensize(4)

for i in range(5):
    pen.left(72)        #angle of rotation calculated by doing(360/n), where n = number of points of the star. It is not the internal angle of the star.
    pen.forward(100)
    #time.sleep(1)
    pen.right(144)      #external angle of rotation.
    pen.forward(100)
    #time.sleep(1)
    
time.sleep(5)

#Note: internal angle = 36
# internal angle of rotation = 72 (as an isosceles triangle is formed by the stars whose one angle connecting the two equal sides is 36)
# external angle of rotation = 144 (i.e 180-36)
