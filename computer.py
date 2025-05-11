"computer.py contains a ComputerPlayer class defining the behavior of the computer in the game."
from set import *
from turn import *
from dice import *


class ComputerPlayer:
    def __init__(self):
        "Kind of AI-based computer player"

        self.turn = False