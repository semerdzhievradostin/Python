from turtle import Turtle, Screen

UP = 90
DOWN = 270
MOVE_DISTANCE = 11


class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(0.7)
        self.turtlesize(stretch_wid=7, stretch_len=1)
        self.color("white")
        self.goto(x, y)
        self.x = 0

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.x, new_y)

    def keybind(self, up, down):
        screen = Screen()
        if up == "w":
            self.x = -350
        else:
            self.x = 350
        screen.onkey(self.up, up)
        screen.onkey(self.down, down)
