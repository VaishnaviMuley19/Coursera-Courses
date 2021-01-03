from turtle import Screen, Turtle
import time

window = Screen()
window.title("Circle")

pen = Turtle()
pen.pensize(4)
pen.speed(0)

for i in range(360):
    pen.left(1)
    pen.forward(1)

for i in range(6):
    for j in range(360):
        pen.right(1)
        pen.forward(1)
    
    for k in range(60):
        pen.left(1)
        pen.forward(1)
    

time.sleep(5)
