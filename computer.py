"computer.py contains a ComputerPlayer class defining the behavior of the computer in the game."
from set import *
from turn import *
from dice import *
from strikes import *
from copy import *


class ComputerPlayer:
    def __init__(self):
        "Kind of AI-based computer player"

        # Boolean to keep track of turns for the computer
        self.turn = False

        # Dice set container for the computer
        self.set_container = SetContainer()

        # List containing the last dice roll the computer did
        self.last_dice_roll = []


        # Total score
        self.total_score = 0

        # Number of rerolls for the computer
        self.max_rerolls = 2

        self.finished = False

        self.remaining_sets = self.set_container.remaining_sets()


        # Dict of possible sets
        self.possible_sets = {}

        # Dict to analyze the last strike (get the number of occurences for each dice)
        self.last_strike_analysis = {}

        # Variable to know if the computer ignored a set on the last turn
        self.has_ignored = False

    def reinitialize_reroll_counter(self):
        "Reinitialize the max reroll counter to 2."
        self.max_rerolls = 2    

    def analyze_strike(self):
        "Analyze the last strike and updates the last strike analyzing dict"
        self.last_strike_analysis = all_dice_occurences(self.last_dice_roll)
        #print("Occurences of all dice :", self.last_strike_analysis)
        return self.last_strike_analysis
    
    def update_score(self):
        "Update the total score based on the computer's set container"
        self.total_score = self.set_container.get_sum()
        
    
    def get_most_frequent_val(self):
        "Returns the value with the highest number of occurencies in the last strike. Returns the lowest value if no result match."
        dice_vals = [dice_val for dice_val in self.last_strike_analysis.keys()]
        most_frequent = min(dice_vals)

        for dice_val in dice_vals:
            if self.last_strike_analysis[dice_val] == max(self.last_strike_analysis.values()):
                most_frequent = dice_val

        return most_frequent        

    

    def update_remaining_sets(self) -> list:
        "Update the list of remaining sets for the computer"
        self.remaining_sets = self.set_container.remaining_sets()
        return self.remaining_sets
    
    def reroll_dice(self, debug=False) -> list:
        "Reroll the dice and returns a list representing the new dice roll"
        # Analyze the last strike
        self.last_strike_analysis = self.analyze_strike()

        # Get the occurrences of each dice value
        occurences_values = self.last_strike_analysis.values()

        # Get the possible sets for the last dice roll
        sets_for_last = possible_sets(self.last_dice_roll)
        
        # Filter the possible sets with those that the computer still have to do
        sets = {dice_set:condition for dice_set, condition in zip(sets_for_last.keys(),sets_for_last.values()) if dice_set in self.set_container.remaining_sets()}

        # We consider the frequent values as those in the superior half of occurences
        frequent_values = [dice_val for dice_val in self.last_strike_analysis.keys()
                           if self.last_strike_analysis[dice_val] in range(max(occurences_values) // 2, max(occurences_values) + 1)]
        
        occurences_frequent = [self.last_strike_analysis[dice_val]for dice_val in self.last_strike_analysis.keys() if self.last_strike_analysis[dice_val]
                               in range(max(occurences_values) // 2, max(occurences_values) + 1)]
        
        #print("Frequent values in the last dice roll :", frequent_values)
        # Get the probability to redo at least one these values

        # Convert the remaining sets into list

        chances_values = chances_dices_values(frequent_values, occurences_frequent, 5 - len(frequent_values))
        if debug:
            print("Chances to redo frequent values :", chances_values)
            print("Probability to redo the exact same dice roll :", probability_dice_roll(frequent_values, occurences_frequent, 5 - len(frequent_values)))
        # Keep only values with max chance to reappear
        middle_chance = max(chances_values.values()) // 2
        max_chance = max(chances_values.values())
        if debug:
            print("Middle chance :", middle_chance)
            print("Max chance :", max_chance)

        max_chances_vals = []
        for val in chances_values.keys():
            if middle_chance <= chances_values[val] and chances_values[val] <= max_chance:
                max_chances_vals.append(val)
        
        if debug:
            print("Values with max chances :", max_chances_vals)

        # Keep values with max chance to reroll
        keep_values = copy(max_chances_vals)

        print("Keeping values :", keep_values)

        # Values to be ignored
        ignored_values = [value for value in self.last_dice_roll if value not in keep_values]


        # Final dice roll
        final_dice = []

        # Extend the final dice roll with the kept dice values
        final_dice.extend(keep_values)
        if debug:
            print("Final dice roll (extended with keep_values):", final_dice)


        # And then add new dice values to it in order to reroll
        final_dice.extend(dice_roll(5 - len(keep_values), ignored_values))


        self.last_dice_roll = copy(final_dice)

        


        return self.last_dice_roll
    

    def decide_ignore(self) -> str:
        """"Decide which strike should be ignored based on last dice roll and remaining sets by determining which value has the lowest chance to reappear. 
        If no condition match, returns a random dice set among the remaining ones."""

        # Analyze the last strike
        self.last_strike_analysis = self.analyze_strike()

        # Get the chances for each value
        chances_values = chances_dices_values(self.last_strike_analysis.keys(), self.last_strike_analysis.values(), self.max_rerolls)
        
        # Get the value with the lowest chance to redo
        value_lowest_chance = min(chances_values, key=chances_values.get)
        

        # Get the possible sets for the value with lowest chance to reappear
        sets_for_lowest = sets_for_value(value_lowest_chance)

        # Filter the possible sets with those that the computer still have to do
        sets = [dice_set for dice_set in sets_for_lowest if dice_set in self.set_container.remaining_sets()]



        # Summarize the scores for the last dice roll
        score_summary = summarize_potential_scores(self.last_dice_roll)

        # Iterate over each dice set in the score summary
        for dice_set in score_summary.keys():
            # If the dice set won't probably reappear
            if dice_set in sets:
                # If the potential score for the dice set is the lowest available
                if score_summary[dice_set] == min(score_summary.values()):
                    # Then ignore that set
                    return dice_set
        
        # Return a random dice set    
        return random.choice(sets)    


    def decide_strike(self, debug=False) -> tuple:
        "Decide which is the best strike to do next according to various parameters"

        strike = "" # Next set to do


        # Analyze the last strike
        self.last_strike_analysis = self.analyze_strike()

        # Get the dice sets did by the computer
        self.remaining_sets = self.update_remaining_sets()

        # If only one set is remaining
        if len(self.remaining_sets) == 1:
            # Pick this one
            set = self.remaining_sets[0]
            score = summarize_potential_scores(self.last_dice_roll)[set]
            return set, score

        # If several sets are available
        else:
            # Get possible dice sets
            self.possible_sets = possible_sets(self.last_dice_roll)

            #print("Possible sets for the computer :", self.possible_sets)

            # List the most frequent dice values in the last dice roll
            occurences_values = self.last_strike_analysis.values()

            # We consider that the most frequent values are those with occurences in the superior half
            frequent_values = [dice_val for dice_val in self.last_strike_analysis.keys()
                            if self.last_strike_analysis[dice_val] in range(max(occurences_values) // 2, max(occurences_values) + 1)]
            
            occurences_frequent = [self.last_strike_analysis[dice_val]for dice_val in self.last_strike_analysis.keys() if self.last_strike_analysis[dice_val]
                                in range(max(occurences_values) // 2, max(occurences_values) + 1)]
            

            if debug:
                print("Most frequent values in the last computer roll :", frequent_values)
                print("Chances to redo frequent values :", chances_dices_values(frequent_values, occurences_frequent, 5 - len(frequent_values)))
            # Get possible sets for the most frequent values
            potential_sets = []
            filtered_sets = []
            for dice_val in frequent_values:
                potential_sets.extend(sets_for_value(dice_val))

            

            # Filter sets to make them appear only one time in the list
            for dice_set in potential_sets:
                if (potential_sets.count(dice_set) ==1) and (dice_set in self.possible_sets and dice_set in self.remaining_sets):
                    filtered_sets.append(dice_set)

            if debug:
                print("Potential sets for the most frequent values :", filtered_sets)

            score_summary = summarize_potential_scores(self.last_dice_roll)

            set, score = get_max_potential_score_set(self.last_dice_roll)
            #print("Set with max potential score :", set)
            valid_sets = [dice_set for dice_set in self.possible_sets if dice_set in self.remaining_sets]
            if valid_sets:
                # Select the set with the highest potential score
                best_set = max(valid_sets, key=lambda s: score_summary[s])
                score = score_summary[best_set]
                strike = best_set

            else:
                # Fallback : ignore a set
                self.has_ignored = True    


            strike = set
            return (strike, score)







        

            












    

        