import turtle
import pandas
from state_revealer import StateFinder


state_maker = StateFinder()

#SET UP THE DATA TO REFERENCE
states_data = pandas.read_csv("50_states.csv")
#MAKE DATA REFERENCE A LIST
states_d_list = states_data["state"].tolist()


correct_answers = []
answer_coords = []

screen = turtle.Screen()
screen.setup(740, 500)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
# INJECT IMAGE
turtle.shape(image)
    
game_on = True

while game_on:
    #SET UP SCREEN
    answer_state = screen.textinput(title=f"{round(len(correct_answers))}/50 States Correct", prompt="What's another state's name?")
    #CHECK IF ANSWER IS CORRECT
    for index, row in states_data.iterrows():
        if row["state"].title() == answer_state.title():
            correct_answers.append(answer_state.title())
            state_maker.new_state(row["x"], row["y"], answer_state.title())
            # FOR BUG TESTING COORDS print(f'{answer_state}: x = {row["x"]}, y = {row["y"]}')

#CREATE TURTLE WITH NAME AS ANSWER_STATE AND COORDS AS X / Y

    #EXIT CONDITIONS
    if answer_state == "exit":
        print(f"You got", len(correct_answers), "correct answers")
        game_on = False
    if len(correct_answers) >= 50:
        print("YOU WIN!!!")
        game_on = False



#GENERATE ONLY STATES THAT HAVENT BEEN GUESSED BY USER states_to_learn.csv

learning_list = []

for state in states_d_list:
    if state not in correct_answers:
        learning_list.append(state)

states_to_learn = pandas.DataFrame(learning_list)
states_to_learn.to_csv("states_to_learn.csv", index=False)

#TODO Record guesses in a list to show to player.