from turtle import Turtle  , Screen
import random


is_race_on = False

screen = Screen()
screen.title("Turtle Race Python Program by dollarboysushil")
screen.setup(width=500 , height = 400)
user_bet  = screen.textinput(title="Bet" , prompt="Choose the color of turtle")


colors = ["red" , "yellow" , "green" , "blue" ,  "black"   , "purple" , "ogitrange"]
y_pos = [-70, -40 ,-10 , 20 , 50 , 80 , 110]
turtle_list = []
for i in range(0,7):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    
    timmy.goto(x=-230 , y=y_pos[i])
    turtle_list.append(timmy)
    
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in turtle_list:
        if turtle.xcor() >230:
            is_race_on = False
            win_color = turtle.pencolor()
            
            if user_bet == win_color:
                print("You Won")
                

            else:
                print(f"You Lost, winner is {win_color}")
                


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()