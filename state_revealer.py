from turtle import Turtle

STATE_HOLDER = []

class StateFinder(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")

    def new_state(self, xpos, ypos, name="EXAMPLE"):
        self.teleport(xpos, ypos, fill_gap=False)
        self.write(name, move=False, align='left', font=('Arial', 8, 'bold'))
        STATE_HOLDER.append(self)
        #FOR BUG TESTING OBJECTS CREATED print(STATE_HOLDER)
        return self
