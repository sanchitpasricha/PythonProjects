from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.start_again()
        self.setheading(90)

    def move(self):
        new_ycord = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_ycord)

    def start_again(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
