from turtle import Turtle , Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen  =  Screen()
screen.setup(600 , 600)
screen.bgcolor("black")
screen.title("OG Snake Game by dollarboysushil")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")



is_game_on =  True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with food using distance method

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detect collision with wall
    if snake.head.xcor() > 280  or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor()<-280 :
        is_game_on  = False
        scoreboard.game_over()

    #detect colision with tail
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()