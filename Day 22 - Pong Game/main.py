from turtle import Turtle  , Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.title('Pong by dollarboysushil')
screen.setup(width=800 , height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard= Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up , 'Up')
screen.onkey(r_paddle.go_down , 'Down')

screen.onkey(l_paddle.go_up , 'w')
screen.onkey(l_paddle.go_down , 's')


game_is_on = True

while game_is_on:  
    time.sleep(0.1)
    screen.update()
    ball.move()

    #collison detection with up and down wall
    if ball.ycor() >275 or ball.ycor()< - 300:
        ball.bounce_y()


    #collision detection with  paddle
    if ball.xcor()>320 and ball.distance(r_paddle) <50 or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()



    if ball.xcor()>380:

        ball.reset_pos()
        scoreboard.l_display()

    
    if  ball.xcor()<-380:
        ball.reset_pos()
        scoreboard.r_display()

screen.exitonclick()