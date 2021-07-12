#this python program creates a red virus
#NOTE: this is not a simulation, just a work of art

from turtle import *

#sets the background color to black
bgcolor('black')

#setting the speed of the turtle
speed(100)

#takes the turtle to an approximate centre of the screen
left(90)
forward(200)
right(90)

#I like my virus red. You can choose any color you prefer
color('red')

#this loop keeps decreasing the edges of the polygon formed by
#increasing the size of edge in each iteration
#the end result looks somewhat like a virus
for x in range(200):
    right(x)
    forward(x*4)

#a temporary program to ensure that our great artwork is visible 
#for some amount of time after it is made
hideturtle()
speed(1)
color('black')
forward(10000)
