import os # to clear screen
from game_classes import Card
from random import randint

def require_confirmation() -> None:
    """ Procedure that requires the user to press enter making sure he reads all that's left behind him on the terminal and then clears screen"""
    
    while input("Press ENTER to continue >> ") != "":
        continue
    os.system('cls||clear')


def show_briscola(briscola_card : Card) -> None:
    """ Procedure that displays the briscola card name and seed """
    print(f"The Briscola card is '{briscola_card.name}' and the Briscola seed is {briscola_card.seed}!\n")


def show_hand(player_hand : list[Card]) -> None:
    """ Procedure that displays the player's hand """

    print("Your hand:")
    for i in range(len(player_hand)):
        print(f"{i+1}. Name: {player_hand[i].name}", end=", ")
        print(f"Value: {player_hand[i].value}", end=", ")
        print(f"Seed: {player_hand[i].seed}")


def choose_card_to_play(player_hand : list[Card]) -> Card:
    """ Function that asks the active player which card to play """

    chosen_card = input(">> Choose a card to play (please enter a number between 1 and 3): ")
    while not chosen_card.isnumeric() or int(chosen_card) not in range(1, len(player_hand) + 1):
        chosen_card = input(">> Choose a valid number: ")
    return player_hand.pop(int(chosen_card) - 1)


def playing_turn(starting_player: int, p1_hand : list[Card], p2_hand : list[Card], table_cards : dict[Card: int]) -> None:
    """ Procedure to lighten the main file code that essentially manages the turn itself """

    if not starting_player: # your case!!
        card1 = choose_card_to_play(p1_hand) # you choose the first card from your hand
        print()
        print(f"You played: {card1.name}")
        table_cards[card1] = starting_player

        card2 = p2_hand.pop(randint(0, len(p2_hand)-1)) # opponent randomly choses a card from his hand
        print(f"Your opponent played: Name: {card2.name}, Value: {card2.value}, Seed: {card2.seed}\n")
        table_cards[card2] = 1

    else: # opponent case
        # TODO implement opponent logic (not in the short term)
        card1 = p2_hand.pop(randint(0, len(p2_hand)-1)) # opponent randomly choses a card from his hand
        print(f"Your opponent played: Name: {card1.name}, Value: {card1.value}, Seed: {card1.seed}")
        table_cards[card1] = starting_player

        card2 = choose_card_to_play(p1_hand) # you choose the card from your hand
        print(f"You played: {card2.name}\n")
        table_cards[card2] = 0
    
    return card1, card2


def check_cards(card1: Card, card2: Card, table_cards : dict[Card: int], briscola_seed) -> int: 
    starting_player = 0

    # case 1: same seed (the simplest, just gotta check the values)
    if card1.seed == card2.seed:
        if card1.value == card2.value: # if they have the same value (0 case) we gotta check the numbers themselves
            if card1.number > card2.number:
                starting_player = table_cards.get(card1)
            else:
                starting_player = table_cards.get(card2)
        elif card1.value > card2.value:
            starting_player = table_cards.get(card1)
        else:
            starting_player = table_cards.get(card2)

        
    # case 2: different seeds
    if card1.seed != card2.seed:
        # this case splits into two
        # 1. one seed is briscola, in that case IT IS gonna win
        # 2. neither is briscola and the one who put the first card takes
            
        if briscola_seed not in [ card.seed for card in table_cards.keys() ]:
            # if there is no BRISCOLA among the two cards, and surely they have not the same seed
            # cause otherwise the other condition would've been true, then the one to take is the first that started
            starting_player = table_cards.get(card1)
        else: # meaning there is a briscola among the two cards
            for card, value in table_cards.items():
                if card.seed == briscola_seed:
                    starting_player = value
                    break 

    return starting_player


def calculate_winner(p1_total_cards : list[Card], p2_total_cards : list[Card]) -> None:
    p1_points = sum( [card.value for card in p1_total_cards] )
    p2_points = sum( [card.value for card in p2_total_cards] )
    
    if p1_points > p2_points:
        print("You won!!! Congrats!")
    elif p2_points > p1_points:
        print("Oh no, you lost :/")
    else:
        print("Incredible!!! A draw!")
    
    print(f"You: {p1_points} points.\nOpponent: {p2_points} points.")
