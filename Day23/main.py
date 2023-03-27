import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

starting_position = (0, -280)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
game_is_on = True
cars = CarManager()
score = Scoreboard()
score.score()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.keybind()
    screen.update()
    cars.create_car()
    cars.move_cars()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.gameover()
            screen.exitonclick()
            game_is_on = False

    if player.is_at_finish():
        player.goto(starting_position)
        score.player_score += 1
        cars.level += 1
        score.clear()
        score.score()






