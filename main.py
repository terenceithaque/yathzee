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

            #print("Possible sets :", player.possible_sets)


            #print("Your remaining sets :", player.remaining_sets)


            # The player can reroll two times max
            max_rerolls = 2

            # Ask the player if he wants to reroll his dice 
            while  max_rerolls > 0:
                
                # If the player wants to reroll
                if ask_reroll():

                    player.reroll_dice()                  
                    max_rerolls -= 1

                # End the loop if he doesn't want to reroll
                else:
                    break


                player.update_remaining_sets()


            # If the player has several sets  to do
            if len(player.possible_sets.keys()) > 1:
                print(f"You must choose between {list(dice_set for dice_set in player.possible_sets if dice_set in 
                                                      player.remaining_sets)}")
                
                # Ask the player which dice set he wants to complete
                dice_set = player.ask_set()
                # Get a summary of the potential scores and extract the score for the chosen dice set
                scores_summary = summarize_potential_scores(player.last_dice_roll)
                score = scores_summary[dice_set]

                # Update the player's set container and the remaining sets
                player.set_container.update(dice_set, score)
                player.update_remaining_sets()

                print("Your game :", player.set_container.content)


            else:
                print(f"You must must end by {player.remaining_sets}")
                
                # Ask the player which dice set he wants to complete
                dice_set = player.ask_set()
                # Get a summary of the potential scores and extract the score for the chosen dice set
                scores_summary = summarize_potential_scores(player.last_dice_roll)
                score = scores_summary[dice_set]

                # Update the player's set container and the remaining sets
                player.set_container.update(dice_set, score)
                player.update_remaining_sets()

                print("Your game :", player.set_container.content)


                       








            change_turn(player, computer_player)

        # If the turn is to the computer
        elif computer_player.turn:
            print("Your computer is playing...")
            computer_player.last_dice_roll = dice_roll(5, [])
            print("Computer roll :", computer_player.last_dice_roll)


            

            #print(computer_player.analyze_strike())

            # Decide the next strike to do
            computer_player.decide_strike()

            # Handle other things below 


            change_turn(player, computer_player)

            #computer_played = True       



# Start the game
play()
        

