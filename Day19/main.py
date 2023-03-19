from turtle import Turtle, Screen, clearscreen, resetscreen

screen = Screen()
screen.setup(width=720, height=720)
bet = screen.textinput("Make your bet", prompt="Which turtle will win the race?Choose a color:  ")
print(bet)
timmy = Turtle()
jimmy = Turtle()
lenny = Turtle()
jenny = Turtle()
kenny = Turtle()

def starting_position():
    # X and Y Coordinates
    timmy.goto(-340, -50)
    jimmy.goto(-340, -100)
    lenny.goto(-340, -150)
    jenny.goto(-340, -200)
    kenny.goto(-340, -250)


starting_position()


screen.exitonclick()