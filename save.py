"save.py handles game save files in JSON format"
import os
import json
import player
import computer

def save(player:player.Player, computer:computer.ComputerPlayer) -> None:
    "Save the data from player and computer into a save.json file."

    # JSON data structure
    data = {
        "player" : {
            "score" : player.total_score,
            "set_container_content": player.set_container.content,
            "remaining_sets": player.set_container.remaining_sets()
        },

        "computer" : {
            "score" : computer.total_score,
            "set_container_content" : computer.set_container.content,
            "remaining_sets" : computer.set_container.remaining_sets()
        }
    }

    # Get the directory of the current script
    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_path = os.path.join(current_dir, "save.json")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)



def load() -> dict:
    "Loads the data inside save.json and makes it accessible to the program."

    # Default data
    data = {
        "player" : {
            "score" : 0,
            "set_container_content":{
            "aces": 0,
            "twos": 0,
            "threes": 0,
            "fours": 0,
            "fives": 0,
            "sixes": 0,
            "3kind": 0,
            "4kind": 0,
            "fullhouse": 0,
            "sm-straight": 0,
            "lg-straight": 0,
            "yathzee": 0,
            "chance": 0
            },

            "remaining_sets": [
            "aces",
            "twos",
            "threes",
            "fours",
            "fives",
            "sixes",
            "3kind",
            "4kind",
            "fullhouse",
            "sm-straight",
            "lg-straight",
            "yathzee",
            "chance"
        ]

        },

        "computer" : {
            "score" : 0,
            "set_container_content":{
            "aces": 0,
            "twos": 0,
            "threes": 0,
            "fours": 0,
            "fives": 0,
            "sixes": 0,
            "3kind": 0,
            "4kind": 0,
            "fullhouse": 0,
            "sm-straight": 0,
            "lg-straight": 0,
            "yathzee": 0,
            "chance": 0
            },

            "remaining_sets": [
            "aces",
            "twos",
            "threes",
            "fours",
            "fives",
            "sixes",
            "3kind",
            "4kind",
            "fullhouse",
            "sm-straight",
            "lg-straight",
            "yathzee",
            "chance"
        ]

        }

    }

    # Get the current script directory
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Construct the path of the save file
    file_path = os.path.join(current_dir, "save.json")

    # If the file exists
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

    # In case of any error
    except:
        # Return the default data
        return data

    return data        