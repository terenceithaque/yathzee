"turn.py allows game turns management"
from dice import *

def change_turn(player, computer):
    """Gives the turn either to the player or the computer according to the last that played a strike."""

    # If the player had the turn on the last strike, then give it to the computer
    if player.turn:
        player.turn = False
        computer.turn=True

    # Or if the computer had the turn on the last strike, then give it to the player
    elif computer.turn:
        computer.turn = False
        player.turn = True


def first_turn(player_roll:list, computer_roll:list) -> int:
    """Determines if either the player or the computer play the first strike based on the sum of a first dice roll.
    Returns 1 for the player, 2 for the computer. If the rolls are equal, then the function first redo them until they're unequal."""

    # Redo the rolls if they're equal
    while sum(player_roll) == sum(computer_roll):
        player_roll = dice_roll()
        computer = dice_roll()


    # If the player has a superior roll sum, then he will begin first
    if sum(player_roll) > sum(computer_roll):
        return 1
    
    # If the computer has a superior roll, sum, then he will begin first
    elif sum(computer_roll) > sum(player_roll):
        return 2
        

    


