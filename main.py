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
def game():
    # Clear hands and reset antes
    jord.reset()
    dan.reset()
    deala.reset()

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
    while (decision == "H" or decision == " ") and jord.hand() < 21:
        dealerOdds = model.dealerProbs(s, [deala.cardsInHand[0]])
        print(dealerOdds)
        # print("Dealer Odds: " + str(dealerOdds))
        decision = model.hitWinOdds(dealerOdds, jord.cardsInHand, s)
        decB = model.hitorstand(s, deala, jord)

        if decision == "S":
            pass
        elif decision == "D":
            jord.ante *= 2
            jord.addCard(s.turnCard())
            pass
        else:
            jord.addCard(s.turnCard())


    print("Jord: " + str(jord.cardsInHand))
    print("Dealer:" + str(deala.cardsInHand[0]))
    print()
    print(decision)
    print(decB)
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

    print(deala.cardsInHand)
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
    elif 21 > jord.hand() > deala.hand():
        # print("Jord wins")
        jord.money += jord.ante
    elif 21 > jord.hand() and deala.hand() > 21:
        # print("Jord wins")
        jord.money += jord.ante
    elif jord.hand() < 21 and jord.hand() == deala.hand():
        # print("Jord Tie")
        pass
    else:
        # print("Jord Loss")
        jord.money -= jord.ante


    if dan.hand() == 21:
        # print("dan Wins")
        dan.money += dan.ante
    elif 21 > dan.hand() > deala.hand():
        # print("Dan wins")
        dan.money += dan.ante
    elif 21 > dan.hand() and deala.hand() > 21:
        # print("Dan Wins")
        dan.money += dan.ante
    elif dan.hand() < 21 and dan.hand() == deala.hand():
        # print("Dan Tie")
        pass
    else:
        # print("Dan Loss")
        dan.money -= dan.ante


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doubleWins = 0

    mon = [0]
    monD = [0]
    t = time.time()
    numGames = 10000

    # Run game specified number of times
    for i in range(numGames):
        # If shoe has fewer than 25 cards left then reshuffle it
        if s.count() < 25:
            s = shoe(5)

        game()

        mon.append(jord.money)
        monD.append(dan.money)

        # if i % (numGames/10) == 0:
        #     print(str(i/(numGames/10)) + "% Finished")

    print(doubles)
    print(sum(doubleOutcomes))
    #
    # print(decisionsA)
    # print(decisionsB)

    plt.plot(range(len(mon)), mon)
    plt.plot(range(len(monD)), monD)
    #plt.legend("Prob Approach", "Following Chart")
    plt.show()
    print(time.time()-t)

