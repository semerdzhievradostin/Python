from turtle import Turtle
POSITIONS = ((0, -300), (0, 300))

class Wall():
    def wall(self):
        for position in POSITIONS:
            wall = Turtle()
            wall.penup()
            wall.shape("square")
            wall.color("white")
            wall.turtlesize(stretch_wid=0.1, stretch_len=300)
            wall.goto(position)



