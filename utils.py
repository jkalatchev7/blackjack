def hand(cardsInHand):
    total = 0
    numAces = 0
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
    total = 0
    numAces = 0
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