from turtle import Screen
from players import Player
from ball import Ball
from walls import Wall
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
player = Player(360, 0)
player2 = Player(-360, 0)
ball = Ball()
wall = Wall()
score = Scoreboard()
wall.wall()

screen.listen()
game_is_on = True
score.score()
while game_is_on:
    player.keybind(up="Up", down="Down")
    player2.keybind(up="w", down="s")
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# Player 2 score
    if ball.xcor() > 360:
        ball.reset_position()
        score.player2_score += 1
        score.score()
# Player 1 score
    if ball.xcor() < -360:
        ball.reset_position()
        score.player1_score += 1
        score.score()
    if ball.distance(player) < 50 and ball.xcor() > 340 or ball.distance(player2) < 50 and ball.xcor() < -340:
        ball.bounce_x()


    screen.update()



screen.exitonclick()
