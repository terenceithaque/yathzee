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

def possible_sets(dice_list:list) -> dict:
    "Returns a dict of possible sets according to the given dice list"

    # A dict of dice sets and the conditions to do them
    sets_conditions = {
        "aces" : 1 in dice_list,
        "twos" : 2 in dice_list,
        "threes" : 3 in dice_list,
        "fours" : 4 in dice_list,
        "fives": 5 in dice_list,
        "sixes" : 6 in dice_list,
        "3kind": any([dice_list.count(dice) >= 3 for dice in dice_list]),
        "4kind" : any([dice_list.count(dice) >= 4  for dice in dice_list]),
        "fullhouse": sorted([dice_list.count(dice) for dice in set(dice_list)]) == [2, 3],

        "sm-straight": any(
        all(val in dice_list for val in seq) for seq in 
        ([1,2,3,4], [2,3,4,5], [3,4,5,6])),
        "lg-straight": any(
        all(val in dice_list for val in seq) for seq in 
        ([1,2,3,4,5], [2,3,4,5,6])),

        "yathzee" : any([dice_list.count(dice) == 5 for dice in dice_list])
    }

    possible_sets = {dice_set:condition for dice_set, condition in sets_conditions.items() if condition}

    return possible_sets





