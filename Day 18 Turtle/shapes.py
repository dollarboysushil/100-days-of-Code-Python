from turtle import Turtle ,  Screen


timmy = Turtle()
timmy.shape("turtle")

for i in range(3):
    timmy.forward(100)
    timmy.right(120)
    
timmy.pencolor("red")

for i in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.pencolor("blue")
for i in range(5):
    timmy.forward(100)
    timmy.right(360/5)
timmy.pencolor("green")
for i in range(6):
    timmy.forward(100)
    timmy.right(360/6)
timmy.pencolor("yellow")
for i in range(7):
    timmy.forward(100)
    timmy.right(360/7)
timmy.pencolor("violet")
for i in range(8):
    timmy.forward(100)
    timmy.right(360/8)
timmy.pencolor("black")
for i in range(9):
    timmy.forward(100)
    timmy.right(360/9)




















screen =  Screen()
screen.exitonclick()