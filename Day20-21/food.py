from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.4)
        self.color("green")
        self.speed("fastest")


    def refresh_location(self):
        x = random.choice(range(-520, 520))
        y = random.choice(range(-230, 230))
        self.goto(x, y)
