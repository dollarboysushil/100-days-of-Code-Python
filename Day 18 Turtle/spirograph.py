import turtle as t
import random


timmy = t.Turtle()
timmy.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_col = (r, g , b)
    return rand_col







def spirograph(gap):
    for i in range(int(360/ gap)):
        timmy.color(random_color())
        timmy.circle(200)
        timmy.setheading(timmy.heading() + gap)
        
    

spirograph(5)

screen = t.exitonclick()