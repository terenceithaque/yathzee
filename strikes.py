"strikes.py handles functions to count probable scores for each dice set."
from dice import *

def count_aces(dice_list:list) -> int:
    """Count the possible score for an aces according to the given dice list"""

    # Count the number of dice with value "1"
    occurences_1 = occurences(dice_list, 1)

    # The possible score is the total of occurences
    score = occurences_1

    return score

def count_twos(dice_list:list) -> int:
    """Count the possible score for a twos according to the given dice list"""

    # Count the number of dice with value "2"
    occurences_2 = occurences(dice_list, 2)

    # The possible score 2 * occurences_2
    score = 2 * occurences_2

    return score


def count_threes(dice_list:list) -> int:
    """Count the possible score for a threes according to the given dice list"""

    # Count the number of dice with value "3"
    occurences_3 = occurences(dice_list, 3)

    # The possible score 3 * occurences_3
    score = 3 * occurences_3

    return score


def count_fours(dice_list:list) -> int:
    """Count the possible score for a fours according to the given dice list"""

    # Count the number of dice with value "4"
    occurences_4 = occurences(dice_list, 4)

    # The possible score 4 * occurences_4
    score = 4 * occurences_4

    return score

def count_fives(dice_list:list) -> int:
    """Count the possible score for a fives according to the given dice list"""

    # Count the number of dice with value "5"
    occurences_5 = occurences(dice_list, 5)

    # The possible score 5 * occurences_5
    score = 5 * occurences_5

    return score


def count_sixes(dice_list:list) -> int:
    """Count the possible score for a sixes according to the given dice list"""

    # Count the number of dice with value "6"
    occurences_6 = occurences(dice_list, 6)

    # The possible score 6 * occurences_6
    score = 6 * occurences_6

    return score


def count_3kind(dice_list: list) -> int:
    """Count the score for a 3-of-a-kind, summing all dice if valid, else 0"""
    for dice_value in set(dice_list):
        if occurences(dice_list, dice_value) >= 3:
            return sum(dice_list)
    return 0


def count_4kind(dice_list: list) -> int:
    """Count the score for a 4-of-a-kind, summing all dice if valid, else 0"""
    for dice_value in set(dice_list):
        if occurences(dice_list, dice_value) >= 4:
            return sum(dice_list)
    return 0


def count_fullhouse() -> int:
    "Count the score for a fullhouse"

    # A fullhouse counts for 25 points
    return 25


def count_smstraight() -> int:
    "Count the score for a small straight"

    # A small straight counts for 30 points
    return 30

def count_lgstraight() -> int:
    "Count the score for a large straight"

    # A large straight counts for 40 points
    return 40


def count_yathzee() -> int:
    "Count the score for a Yathzee"

    # A Yathzee counts for 50 points
    return 50


def count_chance(dice_list) -> int:
    "Count the score for a chance"

    return sum(dice_list)


def summarize_potential_scores(dice_set:list) -> dict:
    """Summarize into a dictionnary the potential scores doable with the given dice set."""

    # Dict summary
    summary = {
        "aces": count_aces(dice_set),
        "twos": count_twos(dice_set),
        "threes": count_threes(dice_set),
        "fours": count_fours(dice_set),
        "fives": count_fives(dice_set),
        "sixes": count_sixes(dice_set),
        "3kind": count_3kind(dice_set),
        "4kind": count_4kind(dice_set),
        "fullhouse": count_fullhouse(),
        "sm-straight": count_smstraight(),
        "lg-straight": count_lgstraight(),
        "yathzee": count_yathzee(),
        "chance": count_chance(dice_set)
    }

    return summary