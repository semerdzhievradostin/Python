from turtle import Turtle, Screen


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.left(90)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def keybind(self):
        screen = Screen()
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")



    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
