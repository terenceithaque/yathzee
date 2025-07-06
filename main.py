"main game file"
from dice import *
from turn import *
from set import *
from player import *
from computer import *
import time

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
        player.turn = True
        computer_player.turn = False

    # Or if the computer starts first
    if first == 2:
        print(f"You did a roll score of {sum(player.last_dice_roll)} against {sum(computer_player.last_dice_roll)} for the computer. Your computer begin first.")
        player.turn = False
        computer_player.turn = True


    # Variables to track if the player and the computer completed all their sets
    player_finished = False
    computer_finished = False    


    # Enter the main loop
    while not (player_finished and computer_finished):
        # If the turn is to the player

        print()

        # If the player haven't completed all his sets
        if not player_finished:
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


                # If the player has several sets  to do and that some of them are doable
                doable_sets = list(dice_set for dice_set in player.possible_sets if dice_set in player.remaining_sets)
                if len(player.possible_sets.keys()) > 1 and len(doable_sets) >= 1:
                    print(f"You must choose between {doable_sets}")
                    
                    # Ask the player which dice set he wants to complete
                    dice_set = player.ask_set()

                    if dice_set != "ignore":
                        # Get a summary of the potential scores and extract the score for the chosen dice set
                        scores_summary = summarize_potential_scores(player.last_dice_roll)
                        score = scores_summary[dice_set]

                        # Update the player's set container and the remaining sets
                        player.set_container.update(dice_set, score)
                        player.update_remaining_sets()

                        #print("Your game :", player.set_container.content)
                        


                else:
                    last_set = player.remaining_sets[0]
                    # If the player can do the last set
                    if last_set in possible_sets(player.last_dice_roll):

                        print(f"You must must end by {player.remaining_sets}")
                    
                        # Ask the player which dice set he wants to complete
                        dice_set = player.ask_set()
                        # Get a summary of the potential scores and extract the score for the chosen dice set
                        scores_summary = summarize_potential_scores(player.last_dice_roll)
                        score = scores_summary[dice_set]

                        # Update the player's set container and the remaining sets
                        player.set_container.update(dice_set, score)
                        player.update_remaining_sets()
                    
                    # If he can't, then skip the turn
                    else:
                        print("You're unable to do the last set for now.")
                        time.sleep(1)


                print("Your game board:")
                player.set_container.display()


                        




                # Update the score
                player.update_score()

                print("Your score :", player.total_score)
                player_finished = player.set_container.is_complete()

                change_turn(player, computer_player)

                

        else:
            print("You completed all your dice sets.")
            time.sleep(1)     

        # If the turn is to the computer
        if not computer_finished:
            if computer_player.turn:
                print("Your computer is playing...")
                computer_player.last_dice_roll = dice_roll(5, [])
                time.sleep(1)
                print("Computer roll :", computer_player.last_dice_roll)

                print("Remaining sets for the computer: ", computer_player.set_container.remaining_sets())

                max_rerolls = 2 # Number of rerolls the computer can do

                print("Set that might be ignored :", computer_player.decide_ignore())
                

                #print(computer_player.analyze_strike())

                # Decide the next strike to do
                dice_set, score = computer_player.decide_strike()

                #computer_player.reroll_dice()

                # List of doable sets
                doable_sets = list(dice_set for dice_set in computer_player.possible_sets if dice_set in computer_player.remaining_sets)

                # Ensure the chosen set wasn't done before
                while dice_set not in computer_player.set_container.remaining_sets():
                    
                    # Reroll the dice
                    if max_rerolls > 0:
                        print("Computer is rerolling...")
                        computer_player.reroll_dice(max_rerolls)
                        print("Computer roll :", computer_player.last_dice_roll)
                        max_rerolls -= 1
                        time.sleep(1)
                        dice_set, score = computer_player.decide_strike()
                        print("New decision :", dice_set)
                        print("Set that might be ignored :", computer_player.decide_ignore())
                        time.sleep(1)

                    else:
                        
                        break    

                

                # Fallback condition if the computer failed to decide a remaining set within 2 dice rolls
                if dice_set not in computer_player.set_container.remaining_sets():
                    # If at least one set is doable
                    if len(doable_sets) >= 1:
                        print("No remaining rerolls, choosing another set.")
                        dice_set = random.choice(doable_sets)
                        score = summarize_potential_scores(computer_player.last_dice_roll)[dice_set]
                        print("New decision :", dice_set)
                        time.sleep(1)

                    # If no set is doable
                    else:
                        # Give the turn to the player
                        print("Computer is unable to do a set, skipping turn.")
                        change_turn(player, computer_player)
                        pass    

                    


                    
                print("The computer chose ", dice_set)
                time.sleep(1)
                computer_player.set_container.update(dice_set, score)
                #print(computer_player.set_container.content)
                print("Computer game board:")
                computer_player.set_container.display()

                # Handle other things below

                # Update the score
                computer_player.update_score()

                print("Your computer's score :", computer_player.total_score)

                computer_finished = computer_player.set_container.is_complete() 


                change_turn(player, computer_player)

                #computer_played = True

        else:
            print("Computer completed all his dice sets.")
            time.sleep(1)       



# Start the game
play()
        

