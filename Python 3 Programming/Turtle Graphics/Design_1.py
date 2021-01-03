from turtle import Screen, Turtle
import time

window = Screen()
window.title("Design 1")

pen = Turtle()
pen.pensize(4)
pen.speed(0)                     #We can set the speed of the pen, 0 is fastest, 10 is fast, 6 is normal, 3 is slow and 1 is slowest


for i in range(36):
    pen.left(10)
    pen.forward(30)
    
    for j in range(22):
        pen.right(10)
        pen.forward(1)
    pen.right(45)
    pen.forward(30)
    
    for k in range(22):
        pen.left(10)
        pen.forward(1)
    pen.left(45)

time.sleep(5)



