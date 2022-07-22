class Dealer():
    def __init__(self):
        self.cardsInHand = []

    def reset(self):
        self.cardsInHand = []

    def addCard(self, card):
        self.cardsInHand.append(card)
        return self.cardsInHand