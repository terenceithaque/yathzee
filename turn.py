"turn.py allows game turns management"

def turn(player_turn:bool, computer_turn:bool):
    """Gives the turn either to the player or the computer according to the last that played a strike.
    
    The player_turn and computer_turn booleans allows to determine who played the last strike.
    For example, if it was the player, then player_turn must be True, but False it if was not."""

    # If the player had the turn on the last strike, then give it to the computer
    if player_turn:
        player_turn = False
        computer_turn = True

    # Or if the computer had the turn on the last strike, then give it to the player
    elif computer_turn:
        computer_turn = False
        player_turn = True   