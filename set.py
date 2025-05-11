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
