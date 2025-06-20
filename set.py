"set.py contains a SetContainer class representing a container for dice sets."
from prettytable import *

def sets_for_value(dice_val:int) -> list:
    "Returns a list of sets that might be done with the given dice value"

    assert dice_val in range(1, 7), "Dice value must be between 1 and 6 included"

    values_sets = {
        1: ["aces", "3kind", "4kind", "fullhouse", "sm-straight", "lg-straight", "yathzee", "chance"],
        2: ["twos", "3kind", "4kind", "fullhouse", "sm-straight", "lg-straight", "yathzee", "chance"],
        3: ["threes", "3kind", "4kind", "fullhouse", "sm-straight", "lg-straight", "yathzee", "chance"],
        4: ["fours", "3kind", "4kind", "fullhouse", "sm-straight", "lg-straight", "yathzee", "chance"],
        5: ["fives", "3kind", "4kind", "fullhouse", "sm-straight", "lg-straight", "yathzee", "chance"],
        6: ["sixes", "3kind", "4kind", "fullhouse", "sm-straight", "lg-straight", "yathzee", "chance"] 
    }

    return values_sets[dice_val]

    

class SetContainer:
    
    def __init__(self):
        "A dice set container"
        # The content of the container, with sets and the respective scores
        self.content = {
            "aces" : 0,
            "twos" : 0,
            "threes" : 0,
            "fours" : 0,
            "fives" : 0,
            "sixes" : 0,
            "3kind" : 0,
            "4kind" : 0,
            "fullhouse" : 0,
            "sm-straight": 0,
            "lg-straight": 0,
            "yathzee" : 0,
            "chance" : 0
        }

    def get_sum(self) -> int:
        """Returns the sum of all set scores"""


        # Skip the dice sets being ignored
        self.content_values = [value for value in self.content.values() if value != "ignored"]
        
        # Iterate over the values of the content and return their sum
        return sum(self.content_values)
    
    

    def display(self) -> None:
        "Display the content of the set container as a table with lines and columns. Scores are displayed using ANSI color code based on their values."


        # ANSI color codes
        yellow = "\033[93m"
        red = "\033[91m"
        reset = "\033[0m"


        table = PrettyTable()
        table.field_names = ["Sets ", "Scores"]
        for dice_set, score in zip(self.content.keys(), self.content.values()):

            # Display "ignored" in red
            if score == "ignored":
                colored_score = f"{red}{score}{reset}"


            else:
                # Display scores superior to 0 in yellow
                if score > 0:
                    colored_score = f"{yellow}{score}{reset}"

                # And display null scores normally    
                else:
                    colored_score = f"{reset}{score}"


            table.add_row([dice_set, colored_score])

            
        print(table)


    

    def remaining_sets(self):
        """Returns a list of the remaining sets to be done (those with score 0)."""
        remaining = [dice_set for dice_set in self.content.keys() if self.content[dice_set] == 0]
        return remaining
    
    def ignore(self, dice_set:str):
        "Defines a dice set as ignored (not equal to 0 in score but simply to be skipped)"

        # Assertions
        assert (type(dice_set).__name__ == "str"), "The set must be a valid string."
        assert (dice_set in self.content.keys()), "Cannot define an unknown dice set as ignored"

        self.content[dice_set] = "ignored"
    
    def update(self, dice_set:str, score:int):
        """Updates the the content of the container using the given set and the associated score value."""

        # Assertions
        assert (type(dice_set).__name__ == "str"), "The set must be a valid string."
        assert (type(score).__name__ == "int"), "The score must be a valid integer."

        assert (dice_set in self.content.keys()), "Cannot modify an unexisting set into a SetContainer."


        # Update the SetContainer
        self.content[dice_set] = score


    def is_complete(self) -> bool:
        "Returns True if all the sets were completed, and False if not. The ignored sets are skipped."

        # Skip the ignored sets
        dice_sets = [dice_set for dice_set in self.content.keys() if self.content[dice_set] != "ignored"]

        return all([self.content[dice_set] > 0 for dice_set in dice_sets])



