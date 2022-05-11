import turtle
from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]

draw = Turtle()
turtle.colormode(255)
draw.speed(20)


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


draw.width(10)
for i in range(2400):
    draw.color(random_rgb())
    draw.forward(10)
    draw.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
