import table_screen
import player_paddle
from pong_ball import PongBall
import score
from score import ScoreBoard
from turtle import Screen

game_is_on = True

#Setting up the field
table = table_screen

#Set up the scoreboards for either player.
scoreboard = ScoreBoard
Player1_score = score.Player1ScoreBoard()
Player2_score = score.Player2ScoreBoard()

#Set up the player paddle avatars.
player_1 = player_paddle.Player1Paddle()
player_2 = player_paddle.Player2Paddle()


#Creating the ball
ball = PongBall()

#Set ball heading
ball.ball_movement()

#Player 1 movement controls
screen = Screen()
def move_up():
    player_1.sety(player_1.ycor() +20)

def move_down():
    current_y = player_1.ycor()
    player_1.sety(player_1.ycor() -20)
    if current_y <= -360:
        print("STOP STOP STOP")
        player_1.sety(-360)

#Player 2 movement controls
def move_up_2():
    player_2.sety(player_2.ycor() +20)

def move_down_2():
    player_2.sety(player_2.ycor() -20)

#Listen for keystrokes for player 1.
screen.onkeypress(move_up, 'w')
screen.onkeypress(move_down, 's')

#Listen for keystrokes for player 2.
screen.listen()
screen.onkeypress(move_up_2, 'Up')
screen.onkeypress(move_down_2, 'Down')



"""GREAT JOB AGAIN!! Now we need to make these settings for player 2!
Then after that we make the ball detect collisions against paddles.
I'm thinking if x and y == x and y of paddle, reverse directions. """

"""Bug log: 
- Only one player at a time can press. Must be a listener issue.
-"""



while game_is_on:
    # Hits the ball into motion
    ball.ball_in_motion()

    # PLAYER 1 COLLISION CONTROL
    if abs(ball.xcor() - player_1.xcor()) < 10 and abs(ball.ycor() - player_1.ycor()) < 55:
        print("COLLISION")
        ball.collision_x()

    #PLAYER 2 COLLISION CONTROL
    if abs(ball.xcor() - player_2.xcor()) < 10 and abs(ball.ycor() - player_2.ycor()) < 55:
        ball.collision_x()

    #If player 1 score.
    if ball.xcor() >= 500:
        ball.player_scored()
        scoreboard.increase_score(Player1_score)
        scoreboard.update_score(Player1_score)
    #If player 2 score.
    if ball.xcor() <= -500:
        ball.player_scored()
        scoreboard.increase_score(Player2_score)
        scoreboard.update_score(Player2_score)







#Keep screen open
table_screen.exit_screen()

