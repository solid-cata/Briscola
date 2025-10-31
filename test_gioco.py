from enum import Enum # importing the enum.Enum class to use enumerations for the card seeds
import random # importing the random library to help in random decision such ad shuffling the cards
import os

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
        self.value = value
        self.name = name

# Now we will create the list of the cards by initiating each one of them
# and then, as the game starts, randomly order the list

cards_names_values = { 1: ('Asso', 11), 2: ('Due', 0), 3: ('Tre', 10), 4: ('Quattro', 0), 5: ('Cinque', 0), 
                     6: ('Sei', 0), 7: ('Sette', 0), 8: ('Fante', 2), 9: ('Cavallo', 3), 10: ('Re', 4) }
cards : list[Card] = []

for seed in Seed:
    for number in range(1, len(cards_names_values)+1):
            value = cards_names_values.get(number)[1]
            name = cards_names_values.get(number)[0]
            cards.append( Card(seed, number, value, name + " di " + seed.name) )


# Creating a Player class
class Player:
    hand : list[Card] # hand of the player that gets updated each turn
    collected_cards : list[Card] # cards collected by the player during the game

    # Default attributes for "hand" and "collected_cards" since they are empty at the beginning
    def __init__(self):
        self.hand = []
        self.collected_cards = []


def require_confirmation() -> None:
    """ Function that requires the user to press enter making sure he reads all that's left behind him on the terminal """
    while input("Press ENTER to continue >> ") != "":
        continue

def clear():
    """ Function that clears the terminal """
    os.system('cls||clear')

def show_hand(player_hand : list[Card]) -> None:
    """ Function that displays the player's hand """
    print("Your hand:")
    for i in range(len(player_hand)):
        print(f"{i+1}. Name: {player_hand[i].name}", end=", ")
        print(f"Value: {player_hand[i].value}", end=", ")
        print(f"Seed: {player_hand[i].seed}")

# defining the "game" function
def game() -> None:
    """ Function that keeps all the game rolling """
    # As the first thing, the cards get shuffled, and the list KEEPS the order like this
    # Of course i could've made a set with all the cards and randomly extract/remove an element,
    # but i wanted to keep it more close to real as possible, since when players draw cards
    # is from the top of the deck (top of the deck in this case will be the end of the list)

    # Shuffling the cards
    random.shuffle(cards)

    # Creating the two players' objects
    p1 = Player() # you!!!
    p2 = Player()

    # Randomly choosing which player will start: 0 for p1, 1 for p2
    who_starts = random.randint(0, 1)

    # Extracting the first 3 cards from the deck and removing them from the list
    # (should be O(1) since we're removing the last element)
    print(f"Player{who_starts + 1} starts first!")
    if not who_starts:
        for _ in range(3):
            p1.hand.append(cards.pop(-1))
        for _ in range(3):
            p2.hand.append(cards.pop(-1))

    else:
        for _ in range(3):
            p2.hand.append(cards.pop(-1))
        for _ in range(3):
            p1.hand.append(cards.pop(-1))

    # Just to stop execution to make the user read
    require_confirmation()

    # Clearing screen (will be using this a lot i think)
    clear()

    show_hand(p1.hand)

    # Now we are goin to extract the "Briscola" card from the top (the end of the list)
    # Once we extract it, though, we are going to insert it at the bottom (the start of the list)
    # since that is how the game works
    
    # Extracting the Briscola card value and its seed
    briscola_card = cards.pop(-1)
    briscola_seed = briscola_card.seed

    print()
    print(f"The Briscola card is '{briscola_card.name}' and the Briscola seed is {briscola_seed}!")

    # Inserting it at the bottom of the deck
    cards.insert(0, briscola_card)
    
    # Starting the game! The first player to start (saved before thanks to the variable) will put a card on the "table"
    # The table will be represented by an array of maximum 2 cards


game()