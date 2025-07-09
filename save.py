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