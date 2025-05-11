"computer.py contains a ComputerPlayer class defining the behavior of the computer in the game."
from set import *
from turn import *
from dice import *


class ComputerPlayer:
    def __init__(self):
        "Kind of AI-based computer player"

        # Boolean to keep track of turns for the computer
        self.turn = False

        # Dice set container for the computer
        self.set_container = SetContainer()

        # List containing the last dice roll the computer did
        self.last_dice_roll = []


        # Total score
        self.total_score = 0


    def dice_occurences(self, dice_value:int) -> int:
        """Returns the number of occurences for a specified dice value in the last dice roll."""
        return self.last_dice_roll.count(dice_value)
    
    def all_dice_occurences(self) -> dict:
        """Returns the number of occurencies for all dice in the last dice roll as a dict."""
        dice_occurences = {}

        for dice in self.last_dice_roll:
            occurences = self.last_dice_roll.count(dice)
            dice_occurences[dice] = occurences

        return dice_occurences    
