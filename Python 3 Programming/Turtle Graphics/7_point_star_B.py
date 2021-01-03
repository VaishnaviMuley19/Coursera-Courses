from turtle import Screen, Turtle
import time

window = Screen()
window.title("7 Points Star")

pen = Turtle()
pen.pensize(4)

pen.left(77.1515)                # internal angle of rotation is 77.1515, it is calculated by three steps
pen.forward(200)
#time.sleep(1)

for i in range(6):
    pen.right(154.286)           # external angle of rotation is 154.286 (i.e 180-25.714), where 25.714 is the internal angle
    pen.forward(200)
        
time.sleep(1)       
