import random
import turtle
from turtle import Turtle, Screen

# import colorgram
#
# extracted_colors = []
# colors = colorgram.extract('image.jpeg', 30)
# for col in colors:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     pallet = (r, g, b)
#     extracted_colors.append(pallet)
#

turtle.colormode(255)
draw = Turtle()

colours_to_use = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40),
                  (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159),
                  (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102),
                  (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39),
                  (164, 209, 187), (151, 206, 220)]

draw.hideturtle()
draw.speed("fastest")
draw.penup()
draw.goto(-250, -250)

for _ in range(10):
    for j in range(10):
        draw.dot(20, random.choice(colours_to_use))
        draw.forward(50)
    draw.setheading(90)
    draw.forward(50)
    draw.setheading(180)
    draw.forward(500)
    draw.setheading(0)

screen = Screen()
screen.exitonclick()
