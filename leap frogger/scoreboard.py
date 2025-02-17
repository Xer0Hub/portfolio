from turtle import Turtle

FONT = ("Courier", 19, "normal")
SCORE = 0
#TODO: CREATE SCOREBOARD THAT TRACKS PLAYER CROSSING AND SCORES
#TODO: CREATE A SCREEN THAT SAYS GAME OVER IF PLAYER IS HIT


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('green')
        self.level = SCORE

    def level_tracker(self):
        self.goto(-168, 260)
        self.write(f"LEVEL: {self.level}", False, "right", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("LOSER", False, 'center', FONT)

    def game_is_won(self):
        self.clear()
        self.goto(0,0)
        self.write("YOU WON! HOW IS THIS POSSIBLE?!?!?!", False, 'center', FONT)



