from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

class Player1Paddle(Paddle):
    def __init__(self):
        super().__init__()
        self.teleport(-450, 0)

class Player2Paddle(Paddle):
    def __init__(self):
        super().__init__()
        self.teleport(440, 0)



