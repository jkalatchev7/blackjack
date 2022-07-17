# This is where the game will be run
from shoe import shoe
from player import player
from dealer import dealer
import model
import time
import matplotlib.pyplot as plt
# Initialize deck
from utils import hand, isSoft

s = shoe(5)
jord = player()
dan = player()
deala = dealer()
decisionsA = []
decisionsB = []
doubles = []
doubleOutcomes_d = {"Win":0, "Loss":0, "Push":0}
doubleOutcomes_j = {"Win":0, "Loss":0, "Push":0}


cardCountResults = [0] * 101
def game():
    # Clear hands and reset antes
    jord.reset()
    dan.reset()
    deala.reset()
    cardCount = s.cardCount

    # Draw First Cards
    jord.addCard(s.turnCard())
    dan.addCard(s.turnCard())
    deala.addCard(s.turnCard())

    # Draw Seconds Cards
    jord.addCard(s.turnCard())
    dan.addCard(s.turnCard())
    deala.addCard(s.turnCard())
    
    ## Check for Surrender
    if (hand(dan.cardsInHand) == 15 and deala.cardsInHand[0] == 10) or (hand(dan.cardsInHand) == 16 and deala.cardsInHand[0] in (9,10,'A')): 
        dan.money -= dan.ante / 2
        #return  UPDATE
    if (hand(jord.cardsInHand) == 15 and deala.cardsInHand[0] == 10) or (hand(jord.cardsInHand) == 16 and deala.cardsInHand[0] in (9,10,'A')): 
        jord.money -= jord.ante / 2
        #return  UPDATE

    # Check if dealer has blackjack
    # TODO: Include Insurance Decision Here
    if deala.hand() == 21:
        # print("Dealer has Blackjack")
        jord.money -= jord.ante
        dan.money -= dan.ante
        return

    decision_j = " "
    decB_j = " "
    followedTable = True
    while (decision_j == "H" or decision_j == " ") and jord.hand() < 21:
        #print()
        dealerOdds = model.updatedDealerOdds(s, [deala.cardsInHand[0]])
        #print(dealerOdds)
        # print("Dealer Odds: " + str(dealerOdds))
        decB_j = model.hitorstand(s, deala, jord)
        decision_j = model.hitWinOdds(dealerOdds, jord.cardsInHand, s, decB_j)

        if decision_j != decB_j:
            followedTable = False
            print(dealerOdds)
            print(jord.cardsInHand, deala.cardsInHand[0])
            print(decision_j, decB_j)

        if decision_j == "S":
            pass
        elif decision_j == "D":
            jord.ante *= 2
            jord.addCard(s.turnCard())
            pass
        else:
            jord.addCard(s.turnCard())


    # print("Jord: " + str(jord.cardsInHand))
    # print("Dealer:" + str(deala.cardsInHand[0]))

    decisionsA.append(decision_j)
    decisionsB.append(decB_j)

    decision_d = " "
    while decision_d in ("H", " ") and dan.hand() < 21:
        decision_d = model.hitorstand(s, deala, dan)
        if decision_d == "S": pass
        elif decision_d == "D":
            dan.ante *= 2
            dan.addCard(s.turnCard())
            pass
        else: dan.addCard(s.turnCard())

    # Dealer plays out his hand (Hits on soft 17)
    while deala.hand() <= 17:
        if deala.hand() == 17 and isSoft(deala.cardsInHand):
            deala.addCard(s.turnCard())
        else:
            pass
        deala.addCard(s.turnCard())

    # Check result for Jord
    jord.outcome(deala.cardsInHand, decision_j, doubleOutcomes_j, cardCount, cardCountResults)

    # If decision went against the table then print hands involved
    if not followedTable: print(jord.hand(), deala.hand())

    # Check result for Dan
    dan.outcome(deala.cardsInHand, decision_d, doubleOutcomes_d, cardCount, cardCountResults)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doubleWins = 0

    mon = [0]
    monD = [0]
    t = time.time()
    numGames = 500

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

    #print(doubles)
    print("Double Jord (W-L-D): ", str(doubleOutcomes_j["Wins"]) + "-" + str(doubleOutcomes_j["Loss"]) + "-" + str(doubleOutcomes_j["Push"]))
    print("Double Dan (W-L-D): ", str(doubleOutcomes_d["Wins"]) + "-" + str(doubleOutcomes_d["Loss"]) + "-" + str(doubleOutcomes_d["Push"]))

    print("Above 0: ", sum(cardCountResults[51:]))
    print("Below 0: ", sum(cardCountResults[0:51]))
    plt.plot(range(len(mon)), mon)
    plt.plot(range(len(monD)), monD)
    #plt.legend("Prob Approach", "Following Chart")
    plt.show()
    print(time.time()-t)

    plt.bar(range(-50,51,1), cardCountResults)
    plt.title('+/- vs. card count')
    plt.xlabel('Card Count')
    plt.ylabel('Wins - Losses')
    plt.show()