A Python command-line based Yathzee game.
Warning : this program requires PrettyTable to installed as a Python module.

Here are the rules:

    - You play against the computer
    - The game works by turns. For each turn you have five dice and the right to roll them max three times.
    - The goal is to reach a certain set of dice numbers : twos, sixes, three of a kind, four of a kind, etc. Each set makes you win a certain amount of points.
    - When both you and the computer did every set, both count their total points. The one with the best score wins.


Here are the sets:

    - Aces: at least one dice with value "1". Returns 1 point per "1" dice. The other dice are ignored.
    - Twos: at least one dice with value "2". Returns 2 points per "2" dice. The other dice are ignored.
    - Threes: at least one dice with value "3". Returns 3 points per "3" dice. The other dice are ignored.
    - Fours: at least one dice with value "4". Returns 4 points per "4" dice. The other dice are ignored.
    - Fives: at least one dice with value "5". Returns  points per "5" dice. The other dice are ignored.
    - Sixes: Threes: at least one dice with value "6". Returns 6 points per "6" dice. The other dice are ignored.


And now special sets:

    - 3 of a kind: at least three dices with the same value. Returns the total of all dice values as points.
    - 4 of a kind: at least four dice with the same value. Returns the total of all dice values as points.
    - Full house: Three dice with the same value and two other dice with the same value. Returns 25 points.
    - Small straight: a sequence of four following dice values. Returns 30 points.
    - Large straight: a sequence of five following dice values. Returns 40 points.
    - Yathzee: five dice with the same value. Returns 50 points.
    - Chance: the sum of all five dice. Works a bit like a joker.


When the game ends, the player and the computer must count both their regular set points and their special set points. The total points are regular set points  + sepcial set points.
