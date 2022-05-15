import turtle
import random
from turtle import Turtle, Screen

is_game_on = False
colors = ['red', 'orange', 'green', 'blue', 'pink', 'purple']
positions = [-140, -80, -20, 40, 100, 160]
players = []
screen = Screen()
screen.setup(height=400, width=500)
user_choice = turtle.textinput('bet your bet', 'Choose your turtle')

for i in range(0, 6):
    jack = Turtle(shape='turtle')
    jack.color(colors[i])
    players.append(jack)
    jack.penup()
    jack.goto(x=-230, y=positions[i])

if user_choice:
    is_game_on = True

while is_game_on:

    for turtle in players:
        if turtle.xcor() > 230:
            win_cor = turtle.pencolor()
            is_game_on = False
            if win_cor == user_choice:
                print(f"You've won! color was {win_cor}")
            else:
                print(f"You've lost! color was {win_cor}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
