from turtle import Turtle ,  Screen
import random

timmy = Turtle()

timmy.pencolor("red")
timmy.speed(10)
timmy.pensize(15)
col = ["red" , 'green' , "blue" , "violet" , "Yellow" , "orange" , "black"]
position = [0 ,90 , 180 , 270 ]
for i in range(500):
    
    timmy.forward(50)
    timmy.color(random.choice(col))
    timmy.setheading(random.choice(position))

screen = Screen()
screen.exitonclick()
