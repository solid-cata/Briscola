# Briscola - Italian Trump Card Game

*This is a try of mine to code the italian card game "Briscola".*

## Rules of the Game and Game Progression
1. You use a set of **40 cards**.  These 40 cards include **4 seeds** (we can define seeds as the "class" that represents each group of cards) which are `Spade`, `Denara`, `Bastoni`, `Coppe`.
2. For each seed there are 10 cards that go from the number 1 to 10.  However, the number on the card is different from the actual value it has in-game:  
    - Number 1: 11 points  
    - Number 3: 10 points  
    - Number 10: 4 points  
    - Number 9: 3 points  
    - Number 8: 2 points  
    - Numbers 7, 6, 5, 4, 2: 0 points
3. At the start of the game, a random card gets extracted from the 40 available and its seed becomes the "Briscola seed". This means that ALL the cards with that seed will be able to "take on" the other player's card (unless of some other conditions, which)