class dealer():
    def __init__(self):
        self.cardsInHand = []

    def reset(self):
        self.cardsInHand = []

    def addCard(self, card):
        self.cardsInHand.append(card)
        return self.cardsInHand

    def hand(self):
        total = 0
        numAces = 0
        for i in self.cardsInHand:
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