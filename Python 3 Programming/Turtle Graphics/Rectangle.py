from turtle import Screen, Turtle
import time

#Here we are creating an instance named window of a Screen class, an instance pen of a turtle class and methods like forward(), right() and left() of a turtle class
#We are also using the sleep() method of time module to pause the program for given time seconds

window = Screen()                #Screen() will open a window which will act as a canvas on which we can draw the graphics
pen = Turtle()                   #Turtle() acts as a pen or pencil through which we are going to draw the graphics
time.sleep(1)                    #sleep() will pause the program for 1 seconds

for i in range(2):
    # forward() will move the Turtle() ahead and in forward() we have to give the argument in pixels
    pen.forward(100)
    #sleep() will pause the Turtle() for 1 second
    time.sleep(1)
    # right() will move the Turtle() towards right and in right()/left() we have to give the arguments in degrees
    pen.right(90)
    time.sleep(1)
    pen.forward(50)
    time.sleep(1)
    pen.right(90)



