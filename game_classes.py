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

    def choose_card_to_play(self):
        """ Method that asks Player1 (you) which card to play """
        chosen_card = input(">> Choose a card to play (please enter a number between 1 and 3): ")
        while not chosen_card.isnumeric() or int(chosen_card) not in range(1, len(self.hand) + 1):
            chosen_card = input(">> Choose a valid number: ")
        return self.hand.pop(int(chosen_card) - 1)

    def show_hand(self) -> None:
        """ Method that displays the player's hand """
        print("Your hand:")
        for i in range(len(self.hand)):
            print(f"{i+1}. Name: {self.hand[i].name}", end=", ")
            print(f"Value: {self.hand[i].value}", end=", ")
            print(f"Seed: {self.hand[i].seed}")

# Creating an Opponent class that inherits from Player and just gives an own definition
# of the choose_card_to_play() module
class Opponent(Player):
    def __init__(self):
        Player.__init__(self)

    # In this re-defined method, we want to manage the bot logic
    # to choose a card with a certain criteria
    # We will build an very safe-playing bot, meaning that
    # it will not risk playing high value cards but make sure to take
    # (could become hard difficulty actually hahaha)
    def choose_card_to_play(self, who_starts: int, briscola_seed: Seed, card_played: Card = None):
        # I'll be referring to the bot as "we" 'cause it's easier to write comments
        # and I'm basicaly writing my personal game criteria in a way

        # We need to choose the card based on two major parameters:
        #   1. the cards we have in hand
        #   2. the card that has been played (or if we are the first to play)
        
        # For point 1. we have 3 scenarios
        #   1.1. No briscolas
        #   1.2. One/Two briscola(s)
        #   1.3. All briscolas

        # For point 2. we have 2 scenarios
        #   2.1. We (bot, in this case) starting
        #   2.2. Opponent (you, player) starting

        # Let's first manage the case where YOU start, which is the simplest
        # (at least for the logic we are trying to build)

        # Since we are starting first, we do not want to gift any points
        # to our opponent, that's why, in any case we are going to throw the
        # card with the lowest value

        # Sorting our hand for value because we are going to choose the lowest card most possible
        # If we have no briscolas, then we can go with the lowest value card in our hand
        # Same if we only have briscolas in our hand
        value_sorted_hand = sorted( self.hand, key=lambda card: card.value )
        no_briscolas = all( map( lambda card: card.seed != briscola_seed, self.hand ) )
        only_briscolas = all( map( lambda card: card.seed == briscola_seed, self.hand ) )
        
        candidate_card = value_sorted_hand[0]

        if who_starts:
            # Now point 1.2. is a bit more compilated. We don't want to throw the Briscola card just yet
            # se we are gonna choose the NON Briscola card with the lowest value
            # HOWEVER, if this card is not Briscola but has a high value, we don't want to throw it
            
            # There's no need for another condition here, since we already calculated the other two
            if candidate_card.seed == briscola_seed:
                # seeint the next card that is sure to have an higher value
                # but we hope not as much
                # but if this card has a value higher than 3 then we will take the previous one
                if len(value_sorted_hand) > 1:
                    if not (value_sorted_hand[1] > 3):
                        candidate_card = value_sorted_hand[1]

        else:
            if card_played.value >= 10:
                if card_played.seed == briscola_seed:
                    # If we are in condition 1.3., if our highest value card
                    if only_briscolas:
                        if value_sorted_hand[-1].value > card_played.value:
                            candidate_card = value_sorted_hand[-1]

                    # For condition 1.2. we need to check if our highest value is a briscola
                    # and is higher than the played card
                    else:
                        if value_sorted_hand[-1].seed == briscola_seed and value_sorted_hand[-1].value > card_played.value:
                            candidate_card = value_sorted_hand[-1]
                        elif value_sorted_hand[-1].seed != briscola_seed:
                            candidate_card = value_sorted_hand[0]
                
                else:
                    # Condition 1.1.
                    any_of_same_seed = any( map( lambda card: card.seed == card_played.seed, value_sorted_hand ) )
                    if any_of_same_seed:
                        for card in value_sorted_hand:
                            if card.seed == card_played.seed:
                                if card.value > card_played.value:
                                    candidate_card = card
                    else:
                        if not no_briscolas:
                            for card in value_sorted_hand:
                                if card.seed == briscola_seed:
                                    candidate_card = card
                                    break

        return candidate_card
