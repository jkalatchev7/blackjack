import time

from resources import Player, Dealer, Shoe
from resources.model import hitWinOdds, calc_dealerOdds
from resources.utils import *

"""
This will be the run file for a user playing a game against the dealer
"""

print("Welcome to Blackjack 101! Let's get to it!")
playername = input("Enter your name to begin: ")

p1 = Player.Player(playername)
dealer = Dealer.Dealer()
shoe = Shoe.Shoe(5)
print("Deck has been shuffled, burning the top card: ")
print(shoe.turnCard())

print("Hello " + p1.name)
print("We will begin the game: Press ctrl-C to exit anytime...")
time.sleep(2)
numRound = 0

while True:
    gameover = False
    print("========== Round " + str(numRound) + "=============")
    print("Money remaining: " + str(p1.money))
    p1.reset()
    dealer.reset()
    # Make sure there are at least 25 cards in the shoe
    if shoe.count() < 25:
        shoe = Shoe.Shoe(5)
        print("Deck has been reshuffled, burning the top card: ")
        print(shoe.turnCard())

    p1.ante = int(input("How much would you like to bet?"))
    print("Dealing Hand...")
    p1.addCard(shoe.turnCard())
    dealer.addCard(shoe.turnCard())
    p1.addCard(shoe.turnCard())
    dealer.addCard(shoe.turnCard())

    print("Your hand: " + str(p1.cardsInHand))
    print("Dealer Upcard: " + str(dealer.cardsInHand[0]))

    if handTotal(p1.cardsInHand) == 21:
        print("Congradulations: You've gotten Blackjack")
        p1.money += p1.ante
        gameover = True
        continue

    if handTotal(dealer.cardsInHand) == 21:
        print("You've lost: Dealer has blackjack")
        gameover = True
        p1.money -= p1.ante
        continue

    decision = ""
    while decision not in ("S", "D"):
        print("Expert recommendations: " + str(hitWinOdds(dealer.cardsInHand[0], p1.cardsInHand, shoe, decision)))
        decision = input("Would you like to hit (H), stand (S), or double (D)?")
        if decision == "S":
            pass
        elif decision == "D":
            p1.addCard(shoe.turnCard())
            p1.ante *= 2
        elif decision == "H":
            p1.addCard(shoe.turnCard())
            pass

        print("Hand: " + str(p1.cardsInHand))

        if handTotal(p1.cardsInHand) > 21:
            print("You've gone over: " + str(p1.cardsInHand))
            gameover = True
            break
        elif handTotal(p1.cardsInHand) == 21:
            print("Congratulations you've hit 21: " + str(p1.cardsInHand))
            gameover = True
            break

        # Play out dealer's hand

    if not gameover:
        while handTotal(dealer.cardsInHand) <= 17:
            if handTotal(dealer.cardsInHand) == 17 and isSoft(dealer.cardsInHand):
                dealer.addCard(shoe.turnCard())
                continue
            dealer.addCard(shoe.turnCard())

        print("Dealer Hand: " + str(dealer.cardsInHand))
        cardCountResults = [0] * 101
        print(p1.outcome(dealer.cardsInHand, shoe.cardCount, cardCountResults))
