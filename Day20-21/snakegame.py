from turtle import Screen
from movement import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=1080, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


scoreboard = Scoreboard()
snake = Snake()
food = Food()

snake.create()
screen.listen()
snake.keybind()
game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Check collision with food
    if snake.head.distance(food) < 10:
        food.refresh_location()
        score += 1
        snake.extend()
        scoreboard.score(score)

    # Detect Collision with wall
    if snake.hit():
        scoreboard.gameover()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            scoreboard.gameover()
            game_is_on = False

screen.exitonclick()
