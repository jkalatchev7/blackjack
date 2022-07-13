# This is where the game will be run
from shoe import shoe
from player import player
from dealer import dealer
import model
import time
import matplotlib.pyplot as plt
# Initialize deck
s = shoe(5)
jord = player()
dan = player()
deala = dealer()
decisionsA = []
decisionsB = []
doubles = []
doubleOutcomes = []


cardCountResults = [0] * 101
def game():
    # Clear hands and reset antes
    jord.reset()
    dan.reset()
    deala.reset()
    low = sum(s.numRem[1:6])
    high = s.numRem[0] + s.numRem[-1]
    cardCount = low-high

    # Draw First Cards
    jord.addCard(s.turnCard())
    dan.addCard(s.turnCard())
    deala.addCard(s.turnCard())

    # Draw Seconds Cards
    jord.addCard(s.turnCard())
    dan.addCard(s.turnCard())
    deala.addCard(s.turnCard())

    # Check if dealer has blackjack
    # TODO: Include Insurance Decision Here
    if deala.hand() == 21:
        # print("Dealer has Blackjack")

        jord.money -= jord.ante
        dan.money -= dan.ante
        return

    decision = " "
    decB = " "
    followedTable = True
    while (decision == "H" or decision == " ") and jord.hand() < 21:
        #print()
        dealerOdds = model.updatedDealerOdds(s, [deala.cardsInHand[0]])
        #print(dealerOdds)
        # print("Dealer Odds: " + str(dealerOdds))
        decB = model.hitorstand(s, deala, jord)
        decision = model.hitWinOdds(dealerOdds, jord.cardsInHand, s, decB)

        if decision != decB:
            followedTable = False
            print(dealerOdds)
            print(jord.cardsInHand, deala.cardsInHand[0])
            print(decision, decB)

        if decision == "S":
            pass
        elif decision == "D":
            jord.ante *= 2
            jord.addCard(s.turnCard())
            pass
        else:
            jord.addCard(s.turnCard())


    # print("Jord: " + str(jord.cardsInHand))
    # print("Dealer:" + str(deala.cardsInHand[0]))

    decisionsA.append(decision)
    decisionsB.append(decB)

    decision = " "
    while (decision == "H" or decision == " ") and dan.hand() < 21:
        decision = model.hitorstand(s, deala, dan)
        if decision == "S":
            pass
        elif decision == "D":
            dan.ante *= 2
            dan.addCard(s.turnCard())
            pass

        else:
            dan.addCard(s.turnCard())

    while deala.hand() < 17:
        deala.addCard(s.turnCard())

    # print(deala.cardsInHand)

    # This function is to verify the utility of doubling
    if decision == 'D':
        doubles.append([dan.cardsInHand, dan.hand(), deala.cardsInHand, deala.hand()])
        if deala.hand() > 21:
            doubleOutcomes.append(1)
        elif deala.hand() < dan.hand():
            doubleOutcomes.append(1)
        elif deala.hand() == dan.hand():
            doubleOutcomes.append(0)
        else:
            doubleOutcomes.append(-1)
    # print("Jord: " + str(jord.cardsInHand))
    # print("Dan: " + str(dan.cardsInHand))
    # print("Dealer: " + str(deala.cardsInHand))

    if jord.hand() == 21:
        # print("Jord Wins")
        jord.money += jord.ante
        cardCountResults[51 + cardCount] += 1
    elif 21 > jord.hand() > deala.hand():
        # print("Jord wins")
        jord.money += jord.ante
        cardCountResults[51 + cardCount] += 1
    elif 21 > jord.hand() and deala.hand() > 21:
        # print("Jord wins")
        jord.money += jord.ante
        cardCountResults[51 + cardCount] += 1
    elif jord.hand() < 21 and jord.hand() == deala.hand():
        # print("Jord Tie")
        pass
    else:
        # print("Jord Loss")
        jord.money -= jord.ante
        cardCountResults[51 + cardCount] -= 1

    if not followedTable:
        print(jord.hand(), deala.hand())

    if dan.hand() == 21:
        # print("dan Wins")
        dan.money += dan.ante
        cardCountResults[51 + cardCount] += 1
    elif 21 > dan.hand() > deala.hand():
        # print("Dan wins")
        dan.money += dan.ante
        cardCountResults[51 + cardCount] += 1
    elif 21 > dan.hand() and deala.hand() > 21:
        # print("Dan Wins")
        dan.money += dan.ante
        cardCountResults[51 + cardCount] += 1
    elif dan.hand() < 21 and dan.hand() == deala.hand():
        # print("Dan Tie")
        pass
    else:
        # print("Dan Loss")
        dan.money -= dan.ante
        cardCountResults[51 + cardCount] -= 1


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
    print(sum(doubleOutcomes))

    print(cardCountResults)

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