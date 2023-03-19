from turtle import Turtle, Screen, clearscreen, resetscreen
import random
screen = Screen()
screen.setup(width=800, height=800)
bet = screen.textinput("Make your bet", prompt="Which turtle will win the race?Choose a color:  ")
color_list = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Brown", "Black", "Pink", "Azure3", "CadetBlue",
              "BlueViolet", "LawnGreen", "ivory1", "ivory2"]


position = 0
def prepare_for_race(position=position):
    for n in range(0, 6):
        timmy = Turtle("turtle")
        timmy.penup()
        position -= 50
        timmy.goto(-370, position)
        timmy.color(color_list[n])
    racing = True
    while racing:
        racers = screen.turtles()
        y = racers.ycor()

        if y >= 780:
            racing = False



prepare_for_race()




screen.exitonclick()