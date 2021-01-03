from turtle import Screen, Turtle
import time

window = Screen()
window.title("Square Pattern 2")

pen = Turtle()
pen.pensize(4)
pen.speed(0)

for i in range(25):
    pen.forward(100)
    for j in range(3):
        pen.right(90)
        pen.forward(100)
    
    pen.right(104)
    #time.sleep(1)

time.sleep(5)


