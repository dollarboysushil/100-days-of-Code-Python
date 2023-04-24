from turtle import Turtle , Screen


timmy = Turtle()
timmy.shape("turtle")



for i in range(50):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()



screen = Screen()
screen.exitonclick()