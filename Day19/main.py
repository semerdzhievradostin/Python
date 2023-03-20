from turtle import Turtle, Screen, clearscreen, resetscreen
import random
screen = Screen()
screen.setup(width=800, height=800)
bet = screen.textinput("Make your bet", prompt="Which turtle will win the race?Choose a color:  ")
color_list = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Brown", "Black", "Pink", "Azure3", "CadetBlue",
              "BlueViolet", "LawnGreen", "ivory1", "ivory2"]


position = 0


def racing_turtles(position):
    for n in range(0, 6):
        timmy = Turtle("turtle")
        timmy.penup()
        position -= 50
        timmy.goto(-370, position)
        timmy.color(color_list[n])
    racing = True
    while racing:
        for turtle in screen.turtles():
            turtle.xcor()
            if turtle.xcor() >= 370:
                winner = turtle.color()
                winner = winner[0]
                print(f"{winner} Wins !")
                racing = False
                if winner == bet:
                    print("Congrats you guessed the right one!")
                else:
                    print("Unlucky, try again !")
            else:
                turtle.forward(random.choice(range(5, 25)))


racing_turtles(position)


screen.exitonclick()
