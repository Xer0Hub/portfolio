#Dependancies
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Initializing player and NPCs
player = Player()
car_manager = CarManager()
loop = 0

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")


game_is_on = True
while game_is_on:
    #SCREEN SETTINGS
    time.sleep(0.01)
    screen.update()
    level.level_tracker()

    # STOP BACKWARD MOVEMENT AT BOUNDARY
    if player.ycor() <= (-281):
        player.goto(0, -280)

    #CREATE CARS AND MOVE THEM IN LOOP
    loop += 1
    if loop >= 20:
        car_manager.create_car()
        loop = 0
    car_manager.move_cars()
    #LOSE CONDITION
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

    #WIN CONDITION. CREATE Y FINISH LINE. TELEPORT TURTLE. SPEED UP CARS.
    if player.ycor() > 280:
        player.goto(0, -280)

        car_manager.speed_boost()
        player.level_up()
        level.next_level()

        if level.level == 10:
            game_is_on = False
            level.game_is_won()




screen.exitonclick()