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


def possibleDealerHands(dealerUpCard):
    options = ["A", "2", "3","4","5","6","7","8","9","F"]
    poss = []
    temp = [dealerUpCard[:]]
    while len(temp) != 0:
        current = temp.pop()
        if handTotal(current) < 17 or (handTotal(current) == 17 and isSoft(current)):
            for i in options:
                t = current[:]
                t.append(str(i))

                if (t[0] == 'A' and t[1] == 'F') or (t[0]=='F' and t[1]=='A'):
                    pass
                else:
                    temp.append(t)
        else:
            poss.append("".join(current))

    np.savetxt('../possibleDealerHands/dealer' + dealerUpCard[0] + '.csv', poss, delimiter=",", fmt="%s")


