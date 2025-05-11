"set.py contains a SetContainer class representing a container for dice sets."


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


