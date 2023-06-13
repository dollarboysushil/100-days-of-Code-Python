import turtle
import pandas

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()


screen = turtle.Screen()
screen.screensize(725,491)
screen.title("US state name game")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
guessed_states= []

all_states = data.state.to_list()
print(all_states)
score = 0

while len(guessed_states) < 50 :

    answer = screen.textinput(f"Score: {score }/50 " , "Enter States Names").title()


    if answer.lower() == "exit":
        missing_states= []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    if answer in all_states :
        score += 1
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        timmy.goto(int(state_data.x) ,int(state_data.y))
        timmy.write(answer)
        print("correct")





screen.mainloop()







