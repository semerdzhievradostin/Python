from turtle import Screen
from players import Player
from ball import Ball
from walls import Wall
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
player = Player(360, 0)
player2 = Player(-360, 0)
ball = Ball()
wall = Wall()
wall.wall()
screen.listen()
game_is_on = True
while game_is_on:
    player.keybind(up="Up", down="Down")
    player2.keybind(up="w", down="s")
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player) and ball.xcor() > 330 or ball.distance(player2) and ball.xcor() < -330:
        ball.bounce_x()
    screen.update()



screen.exitonclick()
