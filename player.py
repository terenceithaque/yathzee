"player.py handles the human player"
from set import *
from turn import *
from dice import *
from strikes import *
from copy import *

class Player:
    def __init__(self):
        "A player"

        # Boolean to keep track of turns for the player
        self.turn = True

        # Dice set container for the player
        self.set_container = SetContainer()

        # List for the last dice roll the player did
        self.last_dice_roll = []

        # Total score
        self.total_score = 0

        self.possible_sets =  {}


        self.remaining_sets = self.set_container.remaining_sets()


    def update_remaining_sets(self) -> list:
        "Updates the list of remaining sets for the player"
        self.remaining_sets = self.set_container.remaining_sets()


    def update_score(self):
         "Update the total score based on the values in the player's set container"
         self.total_score = self.set_container.get_sum()    


    def reroll_dice(self):
        "Reroll the dice of the player"
        # Ask which dice values should be keeped
        keep_values = input("Enter the dice values you want to keep, separated by a comma :")

        # If the player wants to reroll all dice
        if keep_values == "all":
             self.last_dice_roll = dice_roll(5)
             self.possible_sets = possible_sets(self.last_dice_roll)
             print("New dice roll :", self.last_dice_roll)
             print("Possible sets :", self.possible_sets)

        # If the player wants to reroll only some dice
        else:     
            while not keep_values.split(","):
                keep_values = input("Enter the dice values you want to keep, separated by a comma :")

            # The dice values must be 1, 2, 3, 4, 5 or 6
            while not all([value in ["1", "2", "3", "4", "5", "6"]] for value in keep_values.split(",")) :
                keep_values = input("Enter the dice values you want to keep, separated by a comma :")
                    
            keep_values = [int(value) for value in keep_values.split(",")]

            # Number of dice to reroll
            n_dice = 5 - len(keep_values)

            print("Number of dice to reroll :", n_dice)

            ignore_values = [value for value in self.last_dice_roll if value not in keep_values]

            rerolled_dice = dice_roll(n_dice, ignore_values)
                    
            final_dice = []

            # Add kept dice values to the final dice list
            for dice_val in keep_values:
                final_dice.append(dice_val)

            # Add the new rerolled dice to the final dice list
            final_dice.extend(rerolled_dice)


            self.last_dice_roll = copy(final_dice)

            self.possible_sets = possible_sets(self.last_dice_roll)
            print("New dice roll :", self.last_dice_roll)
            print("Possible sets :", self.possible_sets)


    def ask_ignore(self):
         "Ask the player which set he wants to ignore, and declares it as ignored into his set container."

         # Print a caution message
         print("CAUTION ! IF YOU DECIDE TO IGNORE A SET, YOU WON'T BE ABLE TO DO IT NEXT.")

         # Input to confirm
         confirm = input("Do you really want to ignore a set  (answer yes or no) ? ")
         
         # Make sure the player answers "yes or no"
         while confirm.strip().lower() not in ["yes", "no"]:
              confirm = input("Do you really want to ignore a set  (answer yes or no) ? ")

         # If the player answered 'yes'
         if confirm.strip().lower() == "yes":
              set_to_ignore = input("Which set do you want to ignore ? (type 'cancel' if you change your mind) :")
              # If the player change his mind
              if set_to_ignore.strip().lower() == "cancel":
                   print("Ignorance canceled.")
                   return
              # Ensure the set to be ignored wasn't done before
              while not set_to_ignore in self.set_container.remaining_sets():
                    print("You cannot ignore a set you have done.")
                    set_to_ignore = input("Which set do you want to ignore ? (type 'cancel' if you change your mind) : ")
                    # If the player change his mind
                    if set_to_ignore.strip().lower() == "cancel":
                        print("Ignorance canceled.")
                        return



              # Tag the chosen set as ignored in the set container
              self.set_container.ignore(set_to_ignore)

         # if the player answered 'no'
         if confirm.strip().lower() == "no":
              print("Ignorance canceled.")
              # Then return to end the function
              return         
              




    def ask_set(self) -> str:
        """Ask the player which dice set to complete. Returns the entered dice set.
        If the entered set is 'ignore', then ask the player which set to ignore."""

        # Ask the player for the name of the set to be completed
        dice_set = input("Which dice set do you want to complete ? ")


        # If the player wants to ignore a set
        if dice_set == "ignore":
             self.ask_ignore()       

        else:
            # Ensure the entered dice set is valid
            while not dice_set in self.set_container.content.keys():
                print("The entered set is invalid")
                # Ask the player for the name of the set to be completed
                dice_set = input("Which dice set do you want to complete ? ")


            # Ensure the entered set is always into the remaining sets and that the current dice roll allows to do it
            while not dice_set in self.remaining_sets and not dice_set in  self.possible_sets:
                print("The entered dice set is not doable with your current dice roll or you already completed that set.")
                # Ask the player for the name of the set to be completed
                dice_set = input("Which dice set do you want to complete ? ")


            # Ensure the player cannot do the same set twice
            while not self.set_container.content[dice_set] == 0 and self.set_container.content[dice_set] != "ignored":
                print("You already did that set.") 
                # Ask the player for the name of the set to be completed
                dice_set = input("Which dice set do you want to complete ? ")

            # If the dice set was tagged as "ignored"
            while self.set_container.content[dice_set] == "ignored":
                 print("You cannot do an ignored dice set.")
                 # Ask the player for the name of the set to be completed
                 dice_set = input("Which dice set do you want to complete ? ")    


       


        return dice_set    
            



