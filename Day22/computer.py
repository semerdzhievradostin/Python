from turtle import Turtle, Screen


POSITIONS = [(-350, 0)]
UP = 90
DOWN = 270
MOVE_DISTANCE = 11


class Computer:
    def __init__(self):
        self.computer = None
        self.create()

    def create(self):
        for position in POSITIONS:
            self.computers(position)

    def computers(self, position):
        self.computer = Turtle("square")
        self.computer.penup()
        self.computer.shapesize(0.7)
        self.computer.turtlesize(stretch_wid=5, stretch_len=1)
        self.computer.color("white")
        self.computer.goto(position)

    def up(self):
        new_y = self.computer.ycor() + 20
        self.computer.goto(-350, new_y)

    def down(self):
        new_y = self.computer.ycor() - 20
        self.computer.goto(-350, new_y)

    def keybind(self):
        screen = Screen()
        screen.onkey(self.up, "w")
        screen.onkey(self.down, "s")
