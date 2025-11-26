from game_classes import Seed, Card, Player, Opponent
# heard this is not good practice but i'll try my best not to give the same name
# to functions and variables in the main file and in other files
from useful_funcs import * 
import random # importing the random library to help in random decision such ad shuffling the cards

# Now we will create the list of the cards by initiating each one of them
# and then, as the game starts, randomly order the list

cards_names_values = { 1: ('Asso', 11), 2: ('Due', 0), 3: ('Tre', 10), 4: ('Quattro', 0), 5: ('Cinque', 0), 
                     6: ('Sei', 0), 7: ('Sette', 0), 8: ('Fante', 2), 9: ('Cavallo', 3), 10: ('Re', 4) }
cards : list[Card] = []

for seed in Seed:
    for number, value in cards_names_values.items():
            points = value[1]
            name = value[0]
            cards.append( Card(seed, number, points, name + " di " + seed.name) )



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
    p1 : Player = Player() # you!!!
    p2 : Player = Opponent()

    # Randomly choosing which player will start: 0 for p1, 1 for p2
    who_starts : int = random.randint(0, 1)

    # Extracting the first 3 cards from the deck and removing them from the list
    # (should be O(1) since we're removing the last element)
    if not who_starts:
        print(f"You start first!!!")
        for _ in range(3):
            p1.hand.append(cards.pop())
        for _ in range(3):
            p2.hand.append(cards.pop())

    else:
        print(f"Player{who_starts + 1} starts first!")
        for _ in range(3):
            p2.hand.append(cards.pop())
        for _ in range(3):
            p1.hand.append(cards.pop())

    # Just to stop execution to make the user read
    require_confirmation()

    # Now we are goin to extract the "Briscola" card from the top (the end of the list)
    # Once we extract it, though, we are going to insert it at the bottom (the start of the list)
    # since that is how the game works
    
    # Extracting the Briscola card value and its seed
    briscola_card = cards.pop()
    briscola_seed = briscola_card.seed

    # Inserting it at the bottom of the deck
    cards.insert(0, briscola_card)
    
    # Starting the game! The first player to start (saved before thanks to the variable) will put a card on the "table"
    # The table will be represented by an array of maximum 2 cards
    for turn in range(20): # there will be a maximum of 20 turns, since every turn is made of 2 cards on the table and the cards are 40
        print(f"Turn {turn + 1}")
        cards_on_table : dict[Card: int] = {} # this dictionary represents who placed the card and what card he placed

        show_briscola(briscola_card)
        p1.show_hand() # showing hand at the start of each turn
        print()

        first_card, second_card = playing_turn(who_starts, p1, p2, cards_on_table)          

        # After playing the actual turn, we are going to check the various condition to decide
        # who is going to win the hand

        who_starts = check_cards(first_card, second_card, cards_on_table, briscola_seed)
        
        # Deciding here who gets the cards
        if not who_starts:
            print("You collected the cards!!!")
            p1.collected_cards.extend(list(cards_on_table.keys()))

            # Drawing first a card from top of the deck
            if len(cards):
                p1.hand.append(cards.pop())
                p2.hand.append(cards.pop())
        else:
            print("Your opponent collected the cards :((")
            p2.collected_cards.extend(list(cards_on_table.keys()))
            
            if len(cards):
                p2.hand.append(cards.pop())
                p1.hand.append(cards.pop())

        print()
        require_confirmation() # before another loop iteration requiring confirmation and clearing screen

    calculate_winner(p1.collected_cards, p2.collected_cards)

if __name__ == "__main__":
    game()
