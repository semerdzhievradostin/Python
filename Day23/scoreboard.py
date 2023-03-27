from turtle import Turtle

FONT = ("Courier", 18, "normal")
STARTING_POSITION = (0, -280)
LEVEL_POSITION = (-250, 250)
GAMEOVER_POSITION = (0, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 1

    def score(self):
        self.clear()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.write(f"Level:{self.player_score}", align="center", font=FONT)

    def gameover(self):
        self.color("black")
        self.hideturtle()
        self.setposition(STARTING_POSITION)
        self.penup()
        self.goto(GAMEOVER_POSITION)
        self.write("Game Over. ", False, align="center", font=("Arial", 18, "bold"))
