"main game file"
from dice import *
from turn import *
from set import *
from player import *
from computer import *


def ask_reroll() -> bool:
    """Ask the player if he wants to reroll his dice.
    Returns False to keep the current dice roll, or True to reroll."""


    reroll = input("Keep your current roll or reroll dice (answer 1 or 2): ")
    
    # The answer must be 1 to keep the current dice roll or 2 to reroll
    while reroll not in ["1", "2"]:
        reroll = input("Keep your current roll or reroll dice (answer 1 or 2): ")

    if reroll == "1":
        return False

    else:
        return True    




 


def play():
    "Game loop"

    player = Player()
    computer_player = ComputerPlayer()
    # The player must press enter to start playing
    input("Please press enter to start the game: ")






    # Determine if the player or the computer play first
    print("Rolling dice to determine who begins...")
    computer_player.last_dice_roll= dice_roll(5, [])
    player.last_dice_roll = dice_roll(5, [])
    

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


    # Enter the main loop
    while not (player.set_container.is_complete() and computer_player.set_container.is_complete()):
        # If the turn is to the player

        print()
        if player.turn:
            input("Enter to make a dice roll :")
            player.last_dice_roll = dice_roll(5, [])
            print("Your roll :", player.last_dice_roll)

            # Get the possible sets for the current dice roll
            player.possible_sets = possible_sets(player.last_dice_roll)

            print("Possible sets :", player.possible_sets)


            # The player can reroll two times max
            max_rerolls = 2

            # Ask the player if he wants to reroll his dice 
            while  max_rerolls > 0:
                
                # If the player wants to reroll
                if ask_reroll():
                    # Ask which dice values should be keeped
                    keep_values = input("Enter the dice values you want to keep, separated by a comma :")
                    # Check if the values aren't separated by a comma, and re-ask if that is the case
                    while not keep_values.split(","):
                        keep_values = input("Enter the dice values you want to keep, separated by a comma :")

                    # The dice values must be 1, 2, 3, 4, 5 or 6
                    while not all([value in ["1", "2", "3", "4", "5", "6"]] for value in keep_values.split(",")):
                        keep_values = input("Enter the dice values you want to keep, separated by a comma :")
                    
                    keep_values = [int(value) for value in keep_values.split(",")]


                    n_dice = input("Number of dice to reroll :")
                    while n_dice not in ["1", "2", "3", "4", "5"]:
                        n_dice = input("Number of dice to reroll :")

                    n_dice = int(n_dice)

                    rerolled_dice = dice_roll(n_dice, keep_values)
                    
                    final_dice = []

                    # Add kept dice values to the final dice list
                    for dice_val in player.last_dice_roll:
                        if dice_val in keep_values:
                            final_dice.append(dice_val)

                    # Add the new rerolled dice to the final dice list
                    final_dice.extend(rerolled_dice)


                    player.last_dice_roll = final_dice

                    player.possible_sets = possible_sets(final_dice)
                    print("New dice roll :", player.last_dice_roll)
                    print("Possible sets :", player.possible_sets)
                    max_rerolls -= 1

                # End the loop if he doesn't want to reroll
                else:
                    break    








            change_turn(player, computer_player)

        # If the turn is to the computer
        elif computer_player.turn:
            print("Your computer is playing...")
            computer_player.last_dice_roll = dice_roll(5, [])
            print("Computer roll :", computer_player.last_dice_roll)


            print("Remaining sets for the computer :", computer_player.remaining_sets)

            # Handle other things below 


            change_turn(player, computer_player)

            #computer_played = True       



# Start the game
play()
        

