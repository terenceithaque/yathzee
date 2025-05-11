"main game file"
from dice import *
from turn import *
from set import *
from player import *
from computer import *





 


def play():
    "Game loop"

    player = Player()
    computer_player = ComputerPlayer()
    # The player must press enter to start playing
    input("Please press enter to start the game: ")






    # Determine if the player or the computer play first
    print("Rolling dice to determine who begins...")
    computer_player.last_dice_roll= dice_roll()
    player.last_dice_roll = dice_roll()
    

    # Get the beginner
    first = first_turn(player.last_dice_roll, computer_player.last_dice_roll)

    print("Computer roll :", computer_player.last_dice_roll)
    print("Your roll :", player.last_dice_roll)

    # If the player starts first
    if first == 1:
        print(f"You did a roll score of {sum(player.last_dice_roll)} against {sum(computer_player.last_dice_roll)} for the computer. You begin first.")
        player.turns = True
        computer_player.turn = False

    # Or if the computer starts first
    if first == 2:
        print(f"You did a roll score of {sum(player.last_dice_roll)} against {sum(computer_player.last_dice_roll)} for the computer. Your computer begin first.")
        player.turn = False
        computer_player.turn = True



# Start the game
play()
        

