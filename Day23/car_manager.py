import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = random.choice(range(2, 7))


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.level = 1

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_start_y = random.choice(range(-240, 240))
            new_car.goto(280, random_start_y)
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT + self.level)




