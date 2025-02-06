from turtle import Screen, Turtle

screen = Screen()
line = Turtle()

#This is the screen and its background variables.
screen.bgcolor("black")
screen.title("The world's highest pong score is 102,480, are you worth anything?")
screen.screensize(600, 800)
screen.delay(0)
line.shape('square')
line.shapesize(0.5)

#This is the lines on the screen.
line.hideturtle()
line.goto(x=0, y=400)
line.setheading(270)
line.penup()
line.color('white')
line.pencolor('white')
line.speed(0)
dotted_space = 400
for _ in range(50):
    line.goto(x=0, y=dotted_space)
    dotted_space -= 30
    line.stamp()

def exit_screen():
    screen.exitonclick()






