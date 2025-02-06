from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, position, align="center"):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.align = align
        self.update_score()

    def update_score(self):
        #Clear the previous score and write current score
        self.clear()
        self.write(self.score, move=False, align=self.align, font=('Arial', 60, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

#Player 1 score.
class Player1ScoreBoard(ScoreBoard):
    def __init__(self):
        #Position Player 1's score top left.
        super().__init__(position=(-40, 300), align='right')

#Player 2 score.
class Player2ScoreBoard(ScoreBoard):
    def __init__(self):
        # Position Player 2's score top left.
        super().__init__(position=(40, 300), align='left')



