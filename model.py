from utils import *
import numpy as np
from shoe import  shoe
softChoices = np.array([
    # A   2   3   4   5   6   7   8   9  10   DEALER
    ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # A, A
    ['H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 2
    ['H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 3
    ['H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 4
    ['H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 5
    ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # A, 6
    ['H', 'S', 'D', 'D', 'D', 'D', 'S', 'S', 'H', 'H'],  # A, 7
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # A, 8
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']])  # A, 9

hardChoices = np.array([
    # A   2   3   4   5   6   7   8   9  10   DEALER
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
        action = softChoices[player.hand() - 12][dealerVal - 1]
        if action == 'D' and not doubleAllowed:
            action = 'H'
        return action
    else:
        # Hard Hand
        if player.hand() < 9:
            return 'H'
        elif player.hand() > 16:
            return 'S'
        else:
            action = hardChoices[player.hand() - 9][dealerVal - 1]
            if action == 'D' and not doubleAllowed:
                action = 'H'
            return action


# def dealerProbs(shoe, dealerUpCard):
#     dealerOutcomes = [0] * 6
#     arr = []
#     probs = []
#     dealerProbabilities = [0] * 6
#     remaining = 0
#     for i in range(10):
#         temp = dealerUpCard[:]
#         if i == 0:
#             temp.append('A')
#         else:
#             temp.append(str(i + 1))
#
#         valueOfHand = hand(temp)
#         if valueOfHand >= 17:
#             prob = likelihood(shoe, temp)
#             arr.append(temp)
#             probs.append(prob)
#             if valueOfHand > 21:
#                 dealerOutcomes[-1] += 1
#                 dealerProbabilities[-1] += prob
#             else:
#                 dealerOutcomes[valueOfHand - 17] += 1
#                 dealerProbabilities[valueOfHand - 17] += prob
#             continue
#         else:
#             for j in range(10):
#                 tempB = temp[:]
#                 if j == 0:
#                     tempB.append('A')
#                 else:
#                     tempB.append(str(j + 1))
#
#                 valueOfHand = hand(tempB)
#                 prob = likelihood(shoe, tempB)
#                 if valueOfHand >= 17:
#                     arr.append(tempB)
#                     probs.append(prob)
#                     if valueOfHand > 21:
#                         dealerOutcomes[-1] += 1
#                         dealerProbabilities[-1] += prob
#                     else:
#                         dealerOutcomes[valueOfHand - 17] += 1
#                         dealerProbabilities[valueOfHand - 17] += prob
#                     continue
#                 else:
#                     for k in range(10):
#                         tempC = tempB[:]
#                         if k == 0:
#                             tempC.append('A')
#                         else:
#                             tempC.append(str(k + 1))
#
#                         valueOfHand = hand(tempC)
#                         prob = likelihood(shoe, tempC)
#                         if valueOfHand >= 17:
#                             arr.append(tempC)
#                             probs.append(prob)
#                             if valueOfHand > 21:
#                                 dealerOutcomes[-1] += 1
#                                 dealerProbabilities[-1] += prob
#                             else:
#                                 dealerOutcomes[valueOfHand - 17] += 1
#                                 dealerProbabilities[valueOfHand - 17] += prob
#                             continue
#                         else:
#                             for l in range(10):
#                                 tempD = tempC[:]
#                                 if l == 0:
#                                     tempD.append('A')
#                                 else:
#                                     tempD.append(str(l + 1))
#
#                                 valueOfHand = hand(tempD)
#                                 prob = likelihood(shoe, tempD)
#                                 if valueOfHand >= 17:
#                                     arr.append(tempD)
#                                     probs.append(prob)
#                                     if valueOfHand > 21:
#                                         dealerOutcomes[-1] += 1
#                                         dealerProbabilities[-1] += prob
#                                     else:
#                                         dealerOutcomes[valueOfHand - 17] += 1
#                                         dealerProbabilities[valueOfHand - 17] += prob
#                                     continue
#                                 else:
#                                     for p in range(10):
#                                         tempE = tempD[:]
#                                         if p == 0:
#                                             tempE.append('A')
#                                         else:
#                                             tempE.append(str(p + 1))
#
#                                         valueOfHand = hand(tempE)
#                                         prob = likelihood(shoe, tempE)
#                                         if valueOfHand >= 17:
#                                             arr.append(tempE)
#                                             probs.append(prob)
#                                             if valueOfHand > 21:
#                                                 dealerOutcomes[-1] += 1
#                                                 dealerProbabilities[-1] += prob
#                                             else:
#                                                 dealerOutcomes[valueOfHand - 17] += 1
#                                                 dealerProbabilities[valueOfHand - 17] += prob
#                                             continue
#                                         else:
#                                             for ii in range(10):
#                                                 tempF = tempE[:]
#                                                 if ii == 0:
#                                                     tempF.append('A')
#                                                 else:
#                                                     tempF.append(str(ii + 1))
#
#                                                 valueOfHand = hand(tempF)
#                                                 prob = likelihood(shoe, tempF)
#                                                 if valueOfHand >= 17:
#                                                     arr.append(tempF)
#                                                     probs.append(prob)
#                                                     if valueOfHand > 21:
#                                                         dealerOutcomes[-1] += 1
#                                                         dealerProbabilities[-1] += prob
#                                                     else:
#                                                         dealerOutcomes[valueOfHand - 17] += 1
#                                                         dealerProbabilities[valueOfHand - 17] += prob
#                                                     continue
#                                                 else:
#                                                     for jj in range(10):
#                                                         tempG = tempF[:]
#                                                         if jj == 0:
#                                                             tempG.append('A')
#                                                         else:
#                                                             tempG.append(str(jj + 1))
#
#                                                         valueOfHand = hand(tempG)
#                                                         prob = likelihood(shoe, tempG)
#                                                         if valueOfHand >= 17:
#                                                             arr.append(tempG)
#                                                             probs.append(prob)
#                                                             if valueOfHand > 21:
#                                                                 dealerOutcomes[-1] += 1
#                                                                 dealerProbabilities[-1] += prob
#                                                             else:
#                                                                 dealerOutcomes[valueOfHand - 17] += 1
#                                                                 dealerProbabilities[valueOfHand - 17] += prob
#                                                             continue
#                                                         else:
#                                                             for kk in range(10):
#                                                                 tempH = tempG[:]
#                                                                 if kk == 0:
#                                                                     tempH.append('A')
#                                                                 else:
#                                                                     tempH.append(str(kk + 1))
#
#                                                                 valueOfHand = hand(tempH)
#                                                                 prob = likelihood(shoe, tempH)
#                                                                 if valueOfHand >= 17:
#                                                                     arr.append(tempH)
#                                                                     probs.append(prob)
#                                                                     if valueOfHand > 21:
#                                                                         dealerOutcomes[-1] += 1
#                                                                         dealerProbabilities[-1] += prob
#                                                                     else:
#                                                                         dealerOutcomes[valueOfHand - 17] += 1
#                                                                         dealerProbabilities[valueOfHand - 17] += prob
#                                                                     continue
#                                                                 else:
#                                                                     remaining += 1
#                                                                     continue
#
#     return dealerProbabilities


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


def updatedDealerOdds(shoe, dealerUpCard):
    dealerUpCard = dealerUpCard[0]
    if dealerUpCard == '10' or dealerUpCard == 'K' or dealerUpCard == 'Q' or dealerUpCard == 'J':
        path = 'data/dealerF.csv'
    else:
        path = 'data/dealer' + str(dealerUpCard) + '.csv'

    dealerHands = np.genfromtxt(path, dtype=np.str_, delimiter=',')

    # Odds of outcomes [17, 18, 19, 20, 21, BUST]
    dealerProbs = [0] * 6

    for possibleHand in dealerHands:
        prob = likelihood(shoe, possibleHand)
        valueOfHand = hand(possibleHand)
        if valueOfHand > 21:
            dealerProbs[-1] += prob
        else:
            dealerProbs[valueOfHand - 17] += prob

    return dealerProbs

def winOdds(dealerOdds, playerCards):
    dealerTotalProbs = dealerOdds[:]
    val = hand(playerCards)
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


def hitWinOdds(dealerOdds, playerCards, s, decTable):
    if hand(playerCards) < 7:
        return 'H'
    currentWinOdds = winOdds(dealerOdds, playerCards)
    #print(currentWinOdds)
    initalExpectedEarnings = currentWinOdds[0] - currentWinOdds[2]
    counts = s.numRem[:]
    totalWin, totalTie, totalLoss = 0, 0, 0
    if hand(playerCards) == 14:
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
    #print([totalWin, totalTie, totalLoss])
    hitEarnings = totalWin - totalLoss
    standEarnings = initalExpectedEarnings
    if len(playerCards) < 3:
        doubleEarnings = hitEarnings * 2
    else:
        doubleEarnings = -1
    earn = [hitEarnings, standEarnings, doubleEarnings]
    i = earn.index(max([hitEarnings, standEarnings, doubleEarnings]))

    possibilities = ['H','S','D']
    dec = possibilities[i]

    if dec != decTable:
        print("Stand: " + str(currentWinOdds))
        print("Hit: " + str([totalWin, totalTie, totalLoss]))
    return dec