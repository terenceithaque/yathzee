"player.py handles the human player"
from set import *
from turn import *
from dice import *

class Player:
    def __init__(self):
        "A player"

        # Boolean to keep track of turns for the player
        self.turn = True

        # Dice set container for the player
        self.set_container = SetContainer()

        # List for the last dice roll the player did
        self.last_dice_roll = []