import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
score = Scoreboard()
car = CarManager()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for vehicle in car.all_cars:
        if player.distance(vehicle) < 25:
            game_is_on = False
            score.over()

    if player.finish_line():
        player.start_again()
        car.speed_up()
        score.increase_level()

screen.exitonclick()
