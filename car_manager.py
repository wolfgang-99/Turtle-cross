from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_SPOT = 280


class Carmanager:

    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_car = []

    def create_car(self):
        randon_chance = random.randint(1, 6)
        if randon_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            color = random.choice(COLORS)
            new_car.color(color)
            y_spot = random.randint(-250, 250)
            new_car.goto(X_SPOT, y_spot)
            self.all_car.append(new_car)

    def move_cars(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT