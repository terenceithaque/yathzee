"computer.py contains a ComputerPlayer class defining the behavior of the computer in the game."
from set import *
from turn import *
from dice import *
from strikes import *


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

        self.remaining_sets = self.set_container.remaining_sets()


        # Dict of possible sets
        self.possible_sets = {}

        # Dict to analyze the last strike (get the number of occurences for each dice)
        self.last_strike_analysis = {}

    def analyze_strike(self):
        "Analyze the last strike and updates the last strike analyzing dict"
        self.last_strike_anlyze = all_dice_occurences(self.last_dice_roll)
        print("Occurences of all dice :", self.last_strike_anlyze)
        return self.last_strike_anlyze
    

    def update_remaining_sets(self) -> list:
        "Update the list of remaining sets for the computer"
        self.remaining_sets = self.set_container.remaining_sets()
        return self.remaining_sets 

    def decide_strike(self):
        "Decide which is the best strike to do next according to various parameters"
        # Analyze the last strike
        self.last_strike_analysis = self.analyze_strike()

        # Get the dice sets did by the computer
        self.remaining_sets = self.update_remaining_sets()

        # Get possible dice sets
        self.possible_sets = possible_sets(self.last_dice_roll)

        print("Possible sets for the computer :", self.possible_sets)

        








    

        