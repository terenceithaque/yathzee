"main game file"
from dice import *


# Game turns for the player and the computer
player_turn = True
computer_turn = False


def turn():
    "Gives the turn either to the player or the computer according to the last that played a strike."

    # If the player had the turn on the last strike, then give it to the computer
    if player_turn:
        player_turn = False
        computer_turn = True

    # Or if the computer had the turn on the last strike, then give it to the player
    elif computer_turn:
        computer_turn = False
        player_turn = True    



