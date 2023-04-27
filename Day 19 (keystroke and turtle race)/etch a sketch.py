from turtle import Turtle , Screen



timmy = Turtle()
screen = Screen()

def forward():
    timmy.forward(20)

def backward():
    timmy.backward(20)

def cou_clock():
    heading = timmy.heading() + 10
    timmy.setheading(heading)

def clock():
    heading = timmy.heading()- 10
    timmy.setheading(heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

    
screen.listen()
screen.onkey( key = "w" , fun=forward)
screen.onkey( key = "s" , fun=backward)
screen.onkey( key = "a" , fun=cou_clock)
screen.onkey( key = "d" , fun=clock)
screen.onkey(clear  , "c" )


screen.exitonclick()