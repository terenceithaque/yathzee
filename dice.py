"dice.py allows dice handling in the game"
import random
import copy


def new_dice(dice_list:list) -> int:
    """Generate a random dice value and adds it to the dice list."""

    # Copy the current dice list
    dice_list_copy = copy.copy(dice_list)

    # Generate a value for the new dice (between 1 and 6 included)
    dice = random.randint(1, 6)

    # Add the new dice to the dice list
    dice_list_copy.append(dice)

    return dice


def dice_roll() -> list:
    """Simulates a dice roll and returns the corresponding dice list"""
    roll =  []

    # Generate five dice with a random value and add them to the roll list

    for _ in range(5):
        dice = new_dice(roll)
        roll.append(dice)

    # Return the dice roll
    return roll    
