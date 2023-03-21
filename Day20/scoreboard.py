from turtle import Turtle, Screen



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()


    def score(self, score):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 200)
        self.clear()
        self.write(f"Score:{score} ", False, align="center", font=("Arial", 10, "bold"))


    def gameover(self):
        self.color("white")
        self.hideturtle()
        self.setposition(0, 0)
        self.penup()
        self.write("Game Over. ", False, align="center", font=("Arial", 10, "bold"))
