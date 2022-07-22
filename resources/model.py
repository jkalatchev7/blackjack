import json

from resources.utils import *
import numpy as np
from resources.Shoe import Shoe

softChoices = np.array([  # H = Hit, S = Stand, D = Double
    # A    2    3    4    5    6    7    8    9   10   DEALER
    ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # A, A
    ['H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 2
    ['H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 3
    ['H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 4
    ['H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 5
    ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 6
    ['H', 'S', 'D', 'D', 'D', 'D', 'S', 'S', 'H', 'H'],  # A, 7
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # A, 8
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']])  # A, 9

hardChoices = np.array([  # H = Hit, S = Stand, D = Double 
    # A    2    3    4    5    6    7    8    9   10   DEALER
    ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # 9
    ['H', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H'],  # 10
    ['H', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],  # 11
    ['H', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],  # 12
    ['H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],  # 13
    ['H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],  # 14
    ['H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],  # 15
    ['H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],  # 16
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # 17
])

splits = np.array([  # Y = Split, N = Don't Split
    # A    2    3    4    5    6    7    8    9   10   DEALER
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],  # A,A
    ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],  # 10,10
    ['N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N'],  # 9,9
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],  # 8,8
    ['N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],  # 7,7
    ['N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],  # 6,6
    ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],  # 5,5
    ['N', 'N', 'N', 'N', 'Y', 'Y', 'N', 'N', 'N', 'N'],  # 4,4
    ['N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],  # 3,3
    ['N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],  # 2,2
])


def value(card):
    try:
        return int(card)
    except Exception as e:
        if card == 'A':
            return 11
        else:
            return 10


# Method to play directly by the table
def hitorstand(shoe, deala, player):
    doubleAllowed = len(player.cardsInHand) <= 2
    dealerCard = deala.cardsInHand[0]
    playerCards = player.cardsInHand
    dealerVal = value(dealerCard)

    if dealerVal == 11:
        dealerVal = 1

    if isSoft(playerCards):
        # Soft Hand
        if handTotal(player.cardsInHand) >= 18:
            return 'S'
        action = softChoices[handTotal(player.cardsInHand) - 12][dealerVal - 1]
        if action == 'D' and not doubleAllowed:
            action = 'H'
        return action
    else:
        # Hard Hand
        if handTotal(player.cardsInHand) < 9:
            return 'H'
        elif handTotal(player.cardsInHand) > 16:
            return 'S'
        else:
            action = hardChoices[handTotal(player.cardsInHand) - 9][dealerVal - 1]
            if action == 'D' and not doubleAllowed:
                action = 'H'
            return action


def likelihood(shoe, hand):
    counts = shoe.numRem[:]
    total = 1
    handTemp = hand[1:]
    for card in handTemp:
        val = value(card) % 10
        prob = counts[val - 1] / sum(counts)
        counts[val - 1] = counts[val - 1] - 1
        total = total * prob

    return total


def calc_dealerOdds(shoe, dealerUpCard):
    dealerUpCard = dealerUpCard[0]
    if dealerUpCard == '10' or dealerUpCard == 'K' or dealerUpCard == 'Q' or dealerUpCard == 'J':
        path = '../possibleDealerHands/dealerF.csv'
    elif dealerUpCard == 'A':
        path = '../possibleDealerHands/dealerA.csv'
    else:
        path = '../possibleDealerHands/dealer' + str(dealerUpCard) + '.csv'
    dealerHands = np.genfromtxt(path, dtype=np.str_, delimiter=',')

    # Odds of outcomes [17, 18, 19, 20, 21, BUST]
    dealerProbs = [0] * 6

    for possibleHand in dealerHands:
        prob = likelihood(shoe, possibleHand)
        valueOfHand = handTotal(possibleHand)
        if valueOfHand > 21:
            dealerProbs[-1] += prob
        else:
            dealerProbs[valueOfHand - 17] += prob

    return dealerProbs


def winOdds(dealerOdds, playerCards):
    dealerTotalProbs = dealerOdds[:]
    val = handTotal(playerCards)
    bustProb = dealerTotalProbs[-1]
    if val > 21:
        win, tie, loss = 0, 0, 1
    elif val == 21:
        win, tie, loss = 1, 0, 0
    elif val < 17:
        win, tie, loss = dealerTotalProbs[-1], 0, 1 - dealerTotalProbs[-1]
    else:
        tie = dealerTotalProbs[val - 17]
        win = sum(dealerTotalProbs[0:val - 17]) + dealerTotalProbs[-1]
        loss = sum(dealerTotalProbs[val - 16:-1])

    return [win, tie, loss]


def hitWinOdds(dealerUpCard, playerCards, s, decTable):
    dealerOdds = calc_dealerOdds(s, [dealerUpCard])
    if handTotal(playerCards) < 7:
        return 'H'
    currentWinOdds = winOdds(dealerOdds, playerCards)
    # print(currentWinOdds)
    initalExpectedEarnings = currentWinOdds[0] - currentWinOdds[2]
    counts = s.numRem[:]
    totalWin, totalTie, totalLoss = 0, 0, 0
    if handTotal(playerCards) == 14:
        pass
    for i in range(10):
        tempCards = playerCards[:]
        if i == 0:
            tempCards.append('A')
        else:
            tempCards.append(str(i + 1))

        win, tie, loss = winOdds(dealerOdds, tempCards)
        val = value(tempCards[-1]) % 10
        prob = counts[val - 1] / sum(counts)
        totalWin += prob * win
        totalTie += prob * tie
        totalLoss += prob * loss
    # print([totalWin, totalTie, totalLoss])
    hitEarnings = totalWin - totalLoss
    standEarnings = initalExpectedEarnings
    if len(playerCards) < 3:
        doubleEarnings = hitEarnings * 2
    else:
        doubleEarnings = -1
    earn = [hitEarnings, standEarnings, doubleEarnings]
    print("Expected returns [H,S,D]: " + str(earn))
    i = earn.index(max([hitEarnings, standEarnings, doubleEarnings]))

    possibilities = ['H', 'S', 'D']
    dec = possibilities[i]

    if dec != decTable:
        # print("Stand: " + str(currentWinOdds))
        # print("Hit: " + str([totalWin, totalTie, totalLoss]))
        pass
    return dec


# Create table
def createTable():
    holder = []
    hardHands, softHands = {}, {}
    options = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    s = Shoe(5)
    prettyHard, prettySoft = np.chararray([9, 10]), np.chararray([10, 10])
    for i in options:
        for j in options:
            for k in options:
                #dealerOdds = calc_dealerOdds(s, [k])
                decision = hitWinOdds([k], [i, j], s, " ")
                val = str(handTotal([i, j]))
                if 'A' in (i, j):  # soft total
                    softHands[str(val) + "-" + k] = decision
                elif i == j:
                    # splits[str([val, k])] = decision
                    continue
                else:  # hard total
                    hardHands[str(val) + "-" + k] = decision
                # holder.append([(i, j), k, decision])

    for i, j in softHands.items():
        print(i, j)
        row = int(i.split("-")[0]) - 12
        try:
            column = int(i.split("-")[1]) - 1
        except Exception as e:
            column = 0
        prettySoft[row, column] = j

    for i, j in hardHands.items():
        row = int(i.split("-")[0]) - 8
        if row < 0 or row > 8:
            continue
        try:
            column = int(i.split("-")[1]) - 1
        except Exception as e:
            column = 0

        prettyHard[row, column] = j

    print(prettySoft)
    print(prettyHard)

    with open('../results/decision-tables/soft.txt', 'w') as convert_file:
        convert_file.write(json.dumps(softHands))

    with open('../results/decision-tables/hard.txt', 'w') as convert_file:
        convert_file.write(json.dumps(hardHands))

    with open('../results/decision-tables/split.txt', 'w') as convert_file:
        convert_file.write(json.dumps(splits))

    print(softHands)
    print(hardHands)
    print(splits)


#createTable()
