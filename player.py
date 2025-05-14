"player.py handles the human player"
from set import *
from turn import *
from dice import *
from strikes import *

class Player:
    def __init__(self):
        "A player"

        # Boolean to keep track of turns for the player
        self.turn = True

        # Dice set container for the player
        self.set_container = SetContainer()

        # List for the last dice roll the player did
        self.last_dice_roll = []

        # Total score
        self.total_score = 0

        self.possible_sets =  {}


        self.remaining_sets = self.set_container.remaining_sets()


    def update_remaining_sets(self) -> list:
        "Updates the list of remaining sets for the player"
        self.remaining_sets = self.set_container.remaining_sets()


    def reroll_dice(self):
        "Reroll the dice of the player"
        # Ask which dice values should be keeped
        keep_values = input("Enter the dice values you want to keep, separated by a comma :")
        while not keep_values.split(","):
                keep_values = input("Enter the dice values you want to keep, separated by a comma :")

                # The dice values must be 1, 2, 3, 4, 5 or 6
                while not all([value in ["1", "2", "3", "4", "5", "6"]] for value in keep_values.split(",")):
                    keep_values = input("Enter the dice values you want to keep, separated by a comma :")
                    
                keep_values = [int(value) for value in keep_values.split(",")]


                n_dice = input("Number of dice to reroll :")
                while n_dice not in ["1", "2", "3", "4", "5"]:
                    n_dice = input("Number of dice to reroll :")

                n_dice = int(n_dice)

                rerolled_dice = dice_roll(n_dice, keep_values)
                    
                final_dice = []

                # Add kept dice values to the final dice list
                for dice_val in self.last_dice_roll:
                    if dice_val in keep_values:
                        final_dice.append(dice_val)

                # Add the new rerolled dice to the final dice list
                final_dice.extend(rerolled_dice)


                self.last_dice_roll = final_dice

        self.possible_sets = possible_sets(self.last_dice_roll)
        print("New dice roll :", self.last_dice_roll)
        print("Possible sets :", self.possible_sets)