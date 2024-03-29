from turtle import Turtle,Screen
import random

screen = Screen()

screen.setup(width = 800 , height= 600)
is_race_on = False

user_bet = screen.textinput(title="Make a bet", prompt="which turtle will win the race? Enter a Color : ")
colors = ["red", "green", "blue", "orange", "yellow", "pink"]
y_positions = [-70 , -40 , -10 , 20 , 50 , 80]
all_turtle = []
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230 , y = y_positions[i])
    all_turtle.append(new_turtle)

if user_bet :
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()

            if win_color == user_bet:
                print(f"You Won , Your bet was ${win_color} turtle")
            else:
                print(f"You lost , Sorry ! {win_color} turtle wins .")    
        random_dist = random.randint(0,10)
        turtle.forward(random_dist)

screen.exitonclick()    




