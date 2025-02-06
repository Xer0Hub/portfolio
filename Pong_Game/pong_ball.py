from turtle import Turtle, Screen
from random import randint

timer = Screen()

class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(5)
        self.color('yellow')
        self.shape('circle')
        self.goto(0, 0)
        self.showturtle()
        self.isvisible()

    #Ball movement properties
    def ball_movement(self):
        ball_direction = randint(0, 180)
        self.setheading(ball_direction)

    #Balls movement speed
    def ball_in_motion(self):
        self.speed(1)
        self.forward(0.2)
        #Handles collisions on Y (roof and floor)
        if self.ycor() >= 480 or self.ycor() <= -480:
            self.collision_y()

    #Collision detection
    def collision_y(self):
        current_heading = self.heading()
        new_heading = 360 - current_heading
        self.setheading(new_heading)

    def collision_x(self):
        current_heading = self.heading()
        random_dir = randint(1, 50)
        new_heading = 180 - current_heading + random_dir
        self.setheading(new_heading)

    def player_scored(self):
        self.teleport(0,0)
        self.ball_movement()





