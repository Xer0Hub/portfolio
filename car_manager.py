from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 2
CURRENT_SPEED = 0

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        rand_color = COLORS[randint(0, 5)]
        rand_pos = randint(-250, 250)
        new_car.penup()
        new_car.goto(350, rand_pos)
        new_car.color(rand_color)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + CURRENT_SPEED)

    def speed_boost(self):
        global MOVE_INCREMENT
        global CURRENT_SPEED
        CURRENT_SPEED += MOVE_INCREMENT





