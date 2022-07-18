# This is where the game will be run
from shoe import shoe
from player import Player
from dealer import dealer
import model
import time
import matplotlib.pyplot as plt

from utils import isSoft, handTotal

s = shoe(5)
jord = Player("Jordan")
jord.followsTable = False
dan = Player("Dan")
deala = dealer()
decisionsA = []
decisionsB = []
doubles = []
doubleOutcomes_d = {"Win":0, "Loss":0, "Push":0}
doubleOutcomes_j = {"Win":0, "Loss":0, "Push":0}

cardCountResults = [0] * 101


def game():
    print("=============== New Game =================")
    # Clear hands and reset antes
    players = [jord, dan, deala]
    cardCount = s.cardCount

    # Reset the player's hands and antes and the dealer's hand
    for player in players:
        player.reset()

    # Pass out cards to everyone (2 players and dealer)
    for i in range(2):
        for player in players:
            player.addCard(s.turnCard())

    print(jord.cardsInHand, dan.cardsInHand, deala.cardsInHand[0])

    # For non-dealer players check for blackjack
    for player in players[0:-1]:
        if handTotal(player.cardsInHand) == 21:
            print("blackjack ", player.name)
            player.cardsInHand = []
            player.money += player.ante * 1.5
            cardCountResults[51 + cardCount] += 1
            players.remove(player)

    # Check if dealer has blackjack
    # TODO: Include Insurance Decision Here
    if handTotal(deala.cardsInHand) == 21:
        print("Dealer Blackjack")
        for player in players[0:-1]:
            player.money -= player.ante
        return

    followedTable = True

    # Play out player hands
    for player in players[0:-1]:
        print(player.name)
        final_decision = " "
        while (final_decision in ("H", " ")) and handTotal(player.cardsInHand) <= 21:
            dealerOdds = model.updatedDealerOdds(s, [deala.cardsInHand[0]])
            # decision_table is basic method: following table
            decision_table = model.hitorstand(s, deala, jord)
            # This is the other method - our calculations
            decision = model.hitWinOdds(dealerOdds, jord.cardsInHand, s, final_decision)

            if player.followsTable:
                final_decision = decision_table
            else:
                final_decision = decision

            # if decision != decision_table:
            #     followedTable = False
            #     print(dealerOdds)
            #     print(jord.cardsInHand, deala.cardsInHand[0])
            #     print(decision, decision_table)

            if final_decision == "S":
                pass
            elif final_decision == "D":
                player.ante *= 2
                player.addCard(s.turnCard())
                pass
            else:
                player.addCard(s.turnCard())

            print(jord.cardsInHand, dan.cardsInHand, deala.cardsInHand[0])
            
        player.lastDecision = final_decision

    for player in players:
        if handTotal(player.cardsInHand) == 21:
            print("21 ", player.name)
            player.cardsInHand = []
            player.money += player.ante
            cardCountResults[51 + cardCount] += 1
            players.remove(player)

    # Dealer plays out his hand (Hits on soft 17)
    while handTotal(deala.cardsInHand) <= 17:
        if handTotal(deala.cardsInHand) == 17 and isSoft(deala.cardsInHand):
            deala.addCard(s.turnCard())
        else:
            pass
        deala.addCard(s.turnCard())

    print(jord.cardsInHand, dan.cardsInHand, deala.cardsInHand)
    # If decision went against the table then print hands involved
    if not followedTable:
        print(handTotal(jord.cardsInHand), handTotal(deala.cardsInHand))


    # Check result for Jord
    print(jord.outcome(deala.cardsInHand, doubleOutcomes_j, cardCount, cardCountResults))

    # Check result for Dan
    print(dan.outcome(deala.cardsInHand, doubleOutcomes_d, cardCount, cardCountResults))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doubleWins = 0

    mon = [0]
    monD = [0]
    t = time.time()
    numGames = 10

    # Run game specified number of times
    for i in range(numGames):
        # If shoe has fewer than 25 cards left then reshuffle it
        if s.count() < 20:
            s = shoe(5)

        game()

        mon.append(jord.money)
        monD.append(dan.money)

        # if i % (numGames/10) == 0:
        #     print(str(i/(numGames/10)) + "% Finished")


    print("Double Jord (W-L-D): ", str(doubleOutcomes_j["Win"]) + "-" + str(doubleOutcomes_j["Loss"]) + "-" + str(doubleOutcomes_j["Push"]))
    print("Double Dan (W-L-D): ", str(doubleOutcomes_d["Win"]) + "-" + str(doubleOutcomes_d["Loss"]) + "-" + str(doubleOutcomes_d["Push"]))

    print("Above 0: ", sum(cardCountResults[51:]))
    print("Below 0: ", sum(cardCountResults[0:51]))
    plt.plot(range(len(mon)), mon)
    plt.plot(range(len(monD)), monD)
    # plt.legend("Prob Approach", "Following Chart")
    plt.show()
    print(time.time() - t)

    plt.bar(range(-50, 51, 1), cardCountResults)
    plt.title('+/- vs. card count')
    plt.xlabel('Card Count')
    plt.ylabel('Wins - Losses')
    plt.show()
