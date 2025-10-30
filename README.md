# Briscola - Italian Trump Card Game

*This is a try of mine to code the italian card game "Briscola".*

## Rules of the Game and Game Progression

### Setup
* You use a set of **40 cards**.  These 40 cards include **4 seeds** (we can define seeds as the "class" that represents each group of cards) which are `Spade`, `Denara`, `Bastoni`, `Coppe`.
* For each seed there are 10 cards that go from the number 1 to 10.  However, the number on the card is different from the actual value it has in-game:
    - 1 -> 11 points
    - 3 -> 10 points  
    - 10 -> 4 points  
    - 9 -> 3 points  
    - 8 -> 2 points  
    - 2, 4, 5, 6, 7 -> 0 points

### Gameplay
* At the start of the game, a random card gets extracted from the 40 available and its seed becomes the "Briscola seed".  
* Each player is then given 3 cards, drafted from the top of the deck (as it will always be for the rest of the game). The first player to start is chosen randomly.
* The player that starts the turn puts down a card from his hand. The other player choses whater to take on the card or allow his opponent to "win the hand". There are various possibilities, depending on the cards in play, which determine who will take them:
    - If both cards have the *same seed*, the higher value wins (*also applies to Briscola cards*).  
    - If one card is the *Briscola card*, it beats any non-Briscola card.  
    - If the cards have *different seeds* and neither is Briscola, the first card wins.
    
### Scoring
* At the end of the game, the player with the *highest number of points* (sum of the values of the cards it collected) *wins*.