from enum import Enum # importing the enum.Enum class to use enumerations for the card seeds
class Seed(Enum):
    DENARA = 1
    SPADE = 2
    BASTONI = 3
    COPPE = 4

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

cards : list[Card] = []
cards_names_values = { 1: ('Asso', 11), 2: ('Due', 0), 3: ('Tre', 10), 4: ('Quattro', 0), 5: ('Cinque', 0), 
                     6: ('Sei', 0), 7: ('Sette', 0), 8: ('Fante', 2), 9: ('Cavallo', 3), 10: ('Re', 4) }
for seed in Seed:
    for number in range(1, len(cards_names_values)+1):
            value = cards_names_values.get(number)[1]
            name = cards_names_values.get(number)[0]
            cards.append( Card(seed, number, value, name + " di " + seed.name) )

for card in cards:
    print(card.name)
    

# Creating a Player class
class Player:
    hand : list[Card]# hand of the player that gets updated each turn

