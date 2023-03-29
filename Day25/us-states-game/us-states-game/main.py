import turtle
from turtle import Turtle, Screen
from checkanswer import CheckAnswers


screen = Screen()
screen.title("Guess the state")
background = "blank_states_img.gif"
screen.addshape(background)
turtle.shape(background)
correct_states = 0
guesses = []
game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state's name? ")
    answer = answer.title()
    answers = CheckAnswers(answer, guesses)
    if answers.correct():
        guesses.append(answer)
        correct_states += 1
    else:
        game_is_on = True






screen.exitonclick()