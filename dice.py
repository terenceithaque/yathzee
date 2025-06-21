"dice.py allows dice handling in the game"
import random
import copy
import math


def construct_dice_list(dice_vals:dict) -> list:
    "Construct a dice list from a dictionnary of dice values and their occurences for each."

    # Assertions
    assert len(dice_vals) == 5, "The dice_vals dict must have five values"
    assert all([type(dice_val).__name__ == "int"] for dice_val in dice_vals.keys()), "dice values must be int"
    assert all([type(occurence).__name__ == "int"] for occurence in dice_vals.values()), "Occurences must be int"

    # Resulting dice list
    dice_list = []

    # For each dice value in the dict
    for dice_val in dice_vals.keys():
        # Add the dice value to the lists by each occurence of it
        dice_list.extend([dice_val] * dice_vals[dice_val])


    return dice_list





def chances_dices_values(dice_vals:list, occurences:list) -> int:
    """Returns a dictionnary containing each dice value in dice_vals and the chance to obtain it using the occurences list and math.comb().
    - dice_vals: list of dice values
    - occurences: list of occurences for the dice values"""

    assert len(dice_vals) == len(occurences),"Length of dice_vals and occurences must be the same."

    chances_values = {}
    for dice_val, n_occ in zip(dice_vals, occurences):
        # The probability is comb(dice_val * n_occ)
        # * (1 / dice faces)**n_occ
        # * (5 / dice faces)
        # ** (dice_val - n_occ)
        chances_values[dice_val] = math.comb(dice_val, n_occ) * (1 / 6)**n_occ * (5/6)**(dice_val - n_occ)

    return chances_values    


def chance_to_get_value(dice_val:int, n:int) -> int:
    """Return the probability for a dice value to appear n times using math.comb().
      Reminder: math.comb() returns how many combinations exists to have n times some value."""
    
    # The probability is comb(dice_val * n)
    # * (1 / dice faces)**n
    # * (5 / dice faces)
    # ** (dice_val - n)

    prob = math.comb(dice_val, n) * (1 / 6)**n * (5/6)**(dice_val - n)
    return prob






def new_dice() -> int:
    """Generate a random dice value bteween 1 and 6"""
    return random.randint(1,6)


def dice_roll(n_dice=5, ignore_values=[]) -> list:
    """Simulates a dice roll and returns the corresponding dice list.
    n_dice : The number of dice to be rolled
    ignore_values: list of dice values not to be generated"""
    roll =  []

    # Generate n_dice dice with a random value and add them to the roll list

    for _ in range(n_dice):
        dice = new_dice()

        # Ensure the dice is not in the values to be ignored
        while dice in ignore_values:
            # Regenerate the dice
            dice = new_dice()

            
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

        "yathzee" : any([dice_list.count(dice) == 5 for dice in dice_list]),
        "chance":True
    }

    possible_sets = {dice_set:condition for dice_set, condition in sets_conditions.items() if condition}

    return possible_sets



def occurences(dice_list:list, dice_val:int) -> int:
    """Returns the number of occurences for the given dice value"""
    return dice_list.count(dice_val)


def all_dice_occurences(dice_list:list) -> dict:
    """Counts occurences for each dice in the dice list and returns a dict {dice_val: occurences}"""

    occurences = {}

    for dice_val in dice_list:
        occurences[dice_val] = dice_list.count(dice_val)

    return occurences    





