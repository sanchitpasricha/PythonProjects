import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
kiki = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


kiki.speed('fastest')

def draw_spiral(size_of_gap):
    for i in range(int(360/ size_of_gap)):
        kiki.color(random_color())
        kiki.circle(100)
        kiki.setheading(kiki.heading() + size_of_gap)

draw_spiral(3)

screen = Screen()
screen.exitonclick()
