from enum import Enum # importing the enum.Enum class to use enumerations for the card seeds

# Just copied this from stackoverflow (https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
# because i wanted coloured text ;)
class bcolors:
    LIGHT_PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    BROWN = "\033[38;5;94m"
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

# Defining a Seed class that contains an enumeration, thought it was cleaner this way since i used it a lot in Java and C++
class Seed(Enum):
    DENARA = bcolors.YELLOW
    SPADE = bcolors.BLUE
    BASTONI = bcolors.BROWN
    COPPE = bcolors.GREEN

    # Overwriting the method __str__ to automatically print coloured at screen
    def __str__(self):
        return f"{self.value}{self.name}{bcolors.ENDC}"

# Creating the Card class
class Card:
    # Each card has some important attributes as...
    seed : Seed # its seed
    number : int
    value : int # its value (must be one of the "allowed values")
    name : str

    def __init__(self, seed, number, value, name):
        self.seed = seed
        self.number = number
        self.value = value
        self.name = name

# Creating a Player class
class Player:
    hand : list[Card] # hand of the player that gets updated each turn
    collected_cards : list[Card] # cards collected by the player during the game

    # Default attributes for "hand" and "collected_cards" since they are empty at the beginning
    def __init__(self):
        self.hand = []
        self.collected_cards = []
