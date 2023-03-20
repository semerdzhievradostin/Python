from turtle import Turtle, Screen
from movement import Snake
import time
screen = Screen()
screen.setup(width=1080, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
snake.create()
screen.listen()

snake.keybind()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()






screen.exitonclick()