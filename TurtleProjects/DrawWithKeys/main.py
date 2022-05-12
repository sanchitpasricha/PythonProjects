from turtle import Turtle, Screen

draw = Turtle()
screen = Screen()

def move():
    draw.forward(10)


def backward():
    draw.backward(10)


def left_turn():
    new_heading = draw.heading() + 10
    draw.setheading(new_heading)


def right_turn():
    new_heading = draw.heading() - 10
    draw.setheading(new_heading)

def clockwise():
    draw.circle(50, 20, 10)

def clear_art():
    draw.clear()
    draw.penup()
    draw.home()
    draw.pendown()


screen.listen()
screen.onkey(key='w', fun=move)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=left_turn)
screen.onkey(key='d', fun=right_turn)
screen.onkey(key='c', fun=clockwise)
screen.onkey(key='space', fun=clear_art)

screen.exitonclick()
