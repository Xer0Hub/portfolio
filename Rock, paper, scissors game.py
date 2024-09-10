#WINS vs LOSSES
wins = 0
losses = 0

import random


while True:

    #Graphics of moves
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    #Value of moves
    rock_value = 1
    paper_value = 2
    scissors_value = 3

    player_input = int(input("Can you beat me 3 times in "
                         "ROCK, PAPER, SCISSORS? If so you will win an epic prize."
                         "Type 1 for ROCK, 2 for PAPER and 3 for SCISSORS\n"))

    #Player move
    if player_input > 3 or player_input <=0:
        print("WRONG CHOICE!")

    elif player_input == rock_value:
        print(rock)
    elif player_input == paper_value:
        print(paper)
    elif player_input == scissors_value:
        print(scissors)
    else:
        print("Invalid input")

    #Computer move
    computer_move = random.randint(1, 3)

    if computer_move == rock_value:
        print(f"Computer chose: {rock}")
    elif computer_move == paper_value:
        print(f"Computer chose: {paper}")
    elif computer_move == scissors_value:
        print(f"Computer chose: {scissors}")

    #Decision making
    if player_input == computer_move:
        print("DRAW!")

    elif (player_input == 1 and computer_move ==3) or \
            (player_input == 2 and computer_move == 1) or \
            (player_input == 3 and computer_move == 2):
        print("YOU WIN!!! :D ")
        wins += 1
        print(f"Your score is now: {wins}")
    else:
        print("YOU LOSE! :( ")
        losses += 1
        print(f"The computer's score is now: {losses}")

    if wins >= 3:
        print("YOU HAVE DEFEATED EVIL AI AND WON THE WORLD.")
        break
    if losses >= 3:
        print("Game over, machines rule the world.")
        break







