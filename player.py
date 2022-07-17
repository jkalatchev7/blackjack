class Player:
    def __init__(self, name="John"):
        self.money = 0
        self.name = name
        self.cardsInHand = []
        self.ante = 0
        self.followsTable = True

    def reset(self):
        self.cardsInHand = []
        self.ante = 5

    def addCard(self, card):
        self.cardsInHand.append(card)
        return self.cardsInHand


