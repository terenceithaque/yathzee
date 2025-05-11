"main game file"
from dice import *
from turn import *
from set import *





 


def play():
    "Game loop"
    # The player must press enter to start playing
    input("Please press enter to start the game: ")


    # Dice roll list for the player and the computer
    player_roll = []
    computer_roll =  []


    # Set containers for the player and the computer
    player_set_container = SetContainer()

    computer_set_container = SetContainer()


    # Determine if the player or the computer play first
    print("Rolling dice to determine who begins...")
    computer_roll = dice_roll()
    player_roll = dice_roll()
    

    # Get the beginner
    first = first_turn(player_roll, computer_roll)

    print("Computer roll :", computer_roll)
    print("Your roll :", player_roll)

    # If the player starts first
    if first == 1:
        print(f"You did a roll score of {sum(player_roll)} against {sum(computer_roll)} for the computer. You begin first.")
        player_turn = True
        computer_turn = False

    # Or if the computer starts first
    if first == 2:
        print(f"You did a roll score of {sum(player_roll)} against {sum(computer_roll)} for the computer. Your computer begin first.")
        player_turn = False
        computer_turn = True



# Start the game
play()
        

