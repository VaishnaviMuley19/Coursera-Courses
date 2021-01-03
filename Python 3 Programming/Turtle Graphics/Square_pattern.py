from turtle import Screen, Turtle
import time

window = Screen()
window.title("4 Squares Pattern")      #title() sets the title of the Screen()
window.bgcolor("Red")                  #bgcolor() sets the color of the Screen()


pen = Turtle()
pen.pensize(4)                         #pensize() sets the size of the Turtle() 
pen.color("Yellow")                    #color() sets the color of the Turtle()

time.sleep(1)

for i in range(3):                     #This range() is for rows
    for j in range(3):                 #This range() is for columns
        for k in range(4):             #This range() is to draw the square
            pen.forward(100)
            pen.right(90)
        
        pen.up()
        pen.forward(110)
        pen.down()
    
    pen.up()
    pen.forward(-330)
    pen.right(90)
    pen.forward(110)
    pen.right(270)
    pen.down()

