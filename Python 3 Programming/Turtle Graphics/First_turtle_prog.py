from turtle import Screen, Turtle
import time

#Here we are creating an instance named window of a Screen class, an instance pen of a turtle class and methods like forward(), right() and left() of a turtle class
#We are also using the sleep() method of time module to pause the program for given time seconds

window = Screen()                #Screen() will open a window which will act as a canvas on which we can draw the graphics
pen = Turtle()                   #Turtle() acts as a pen or pencil through which we are going to draw the graphics
time.sleep(2)                    #sleep() will pause the program for 2 seconds
pen.forward(20)                  #forward() will move the Turtle() ahead and in forward() we have to give the argument in pixels
time.sleep(2)
pen.right(90)                    #right() will move the Turtle() towards right and in right()/left() we have to give the arguments in degrees
pen.forward(20)
time.sleep(2)
pen.left(90)
time.sleep(5)

#Note: Without importing time, if we run the program, we will not be able to see the operations being performed because everything happens in fraction of seconds.
#So, to be able to see the Turtle() to draw the graphics we have to use the sleep() method of time module, which pause the program for the given time and the time is given in seconds.
