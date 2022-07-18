import numpy as np

def handTotal(cardsInHand):
    total, numAces = 0, 0
    for i in cardsInHand:
        try:
            total += int(i)
        except Exception as e:
            if i == 'A':
                numAces += 1
                total += 1
            else:
                total += 10

    while total <= 11 and numAces > 0:
        total += 10
        numAces -= 1

    return total


def isSoft(cardsInHand):
    total, numAces = 0, 0
    ace = False
    for i in cardsInHand:
        try:
            total += int(i)
        except Exception as e:
            if i == 'A':
                numAces += 1
                total += 1
                ace = True
            else:
                total += 10

    while total <= 11 and numAces > 0:
        total += 10
        numAces -= 1
    if numAces > 0:
        return False
    else:
        return ace


# Note "F" implies a card worth 10 (face card or 10)
def possibleHands(dealerUpCard):
    possibleHands = []
    remaining = 0
    dealerOutcomes = [0] * 6
    for i in range(10):
        temp = dealerUpCard[:]
        if i == 0:
            temp.append('A')
        elif i == 9:
            temp.append('F')
        else:
            temp.append(str(i + 1))

        valueOfHand = handTotal(temp)
        if valueOfHand > 17 or (valueOfHand == 17 and not isSoft(temp)):
            possibleHands.append("".join(temp))

        else:
            for j in range(10):
                tempB = temp[:]
                if j == 0:
                    tempB.append('A')
                elif j == 9:
                    tempB.append('F')
                else:
                    tempB.append(str(j + 1))
                valueOfHand = handTotal(tempB)
                if valueOfHand > 17 or (valueOfHand == 17 and not isSoft(temp)):
                    possibleHands.append("".join(tempB))

                else:
                    for k in range(10):
                        tempC = tempB[:]
                        if k == 0:
                            tempC.append('A')
                        elif k == 9:
                            tempC.append('F')
                        else:
                            tempC.append(str(k + 1))

                        valueOfHand = handTotal(tempC)
                        if valueOfHand > 17 or (valueOfHand == 17 and not isSoft(temp)):
                            possibleHands.append("".join(tempC))

                        else:
                            for l in range(10):
                                tempD = tempC[:]
                                if l == 0:
                                    tempD.append('A')
                                elif l == 9:
                                    tempD.append('F')
                                else:
                                    tempD.append(str(l + 1))

                                valueOfHand = handTotal(tempD)

                                if valueOfHand > 17 or (valueOfHand == 17 and not isSoft(temp)):
                                    possibleHands.append("".join(tempD))

                                else:
                                    for p in range(10):
                                        tempE = tempD[:]
                                        if p == 0:
                                            tempE.append('A')
                                        elif p == 9:
                                            tempE.append('F')
                                        else:
                                            tempE.append(str(p + 1))

                                        valueOfHand = handTotal(tempE)

                                        if valueOfHand > 17 or (valueOfHand == 17 and not isSoft(temp)):
                                            possibleHands.append("".join(tempE))

                                        else:
                                            for ii in range(10):
                                                tempF = tempE[:]
                                                if ii == 0:
                                                    tempF.append('A')
                                                elif ii == 9:
                                                    tempF.append('F')
                                                else:
                                                    tempF.append(str(ii + 1))

                                                valueOfHand = handTotal(tempF)

                                                if valueOfHand > 17 or (valueOfHand == 17 and not isSoft(temp)):
                                                    possibleHands.append("".join(tempF))
                                                else:
                                                    for jj in range(10):
                                                        tempG = tempF[:]
                                                        if jj == 0:
                                                            tempG.append('A')
                                                        elif jj == 9:
                                                            tempG.append('F')
                                                        else:
                                                            tempG.append(str(jj + 1))

                                                        valueOfHand = handTotal(tempG)

                                                        if valueOfHand > 17 or (valueOfHand == 17 and not isSoft(temp)):
                                                            possibleHands.append("".join(tempG))

                                                        else:
                                                            for kk in range(10):
                                                                tempH = tempG[:]
                                                                if kk == 0:
                                                                    tempH.append('A')
                                                                elif kk == 9:
                                                                    tempH.append('F')
                                                                else:
                                                                    tempH.append(str(kk + 1))

                                                                valueOfHand = handTotal(tempH)
                                                                if valueOfHand >= 17:
                                                                    possibleHands.append("".join(tempH))

                                                                else:
                                                                    remaining += 1
                                                                    continue

    np.savetxt('data/dealer' + dealerUpCard[0] + '.csv', possibleHands, delimiter=",", fmt="%s")

    return possibleHands


# Method to compute and save the possible hands for each dealer upcard... so we don't have to compute this every time
def createTable():
    possibleHands(['A'])
    possibleHands(['2'])
    possibleHands(['3'])
    possibleHands(['4'])
    possibleHands(['5'])
    possibleHands(['6'])
    possibleHands(['7'])
    possibleHands(['8'])
    possibleHands(['9'])
    possibleHands(['F'])
