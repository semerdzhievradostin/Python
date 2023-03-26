from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player2_score = 0
        self.player1_score = 0

    def score(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-100, 200)
        self.write(self.player2_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player1_score, align="center", font=("Courier", 80, "normal"))
    def gameover(self):
        self.color("white")
        self.hideturtle()
        self.setposition(0, 0)
        self.penup()
        self.write("Game Over. ", False, align="center", font=("Arial", 10, "bold"))
