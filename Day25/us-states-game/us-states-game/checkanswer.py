from turtle import Turtle
import pandas

FONT = ("Courier", 8, "bold")

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
state_x = data["x"].to_list()
state_y = data["y"].to_list()


class CheckAnswers(Turtle):
    def __init__(self, answer, guesses):
        super().__init__()
        self.answers = guesses
        self.answer = answer

    def correct(self):
        for state in states:
            if self.answer in self.answers:
                return False
            elif self.answer == state:
                xcor = state_x[states.index(self.answer)]
                ycor = state_y[states.index(self.answer)]
                self.color("black")
                self.hideturtle()
                self.penup()
                self.goto(xcor, ycor)
                self.write(self.answer, align="center", font=FONT)
                return True
