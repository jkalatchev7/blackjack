import random


class Shoe():
    def __init__(self, numDecks):
        self.shoe = ['A','2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K'] * 4 * numDecks
        self.numRem = [4 * numDecks] * 10
        self.numRem[9] = self.numRem[9] * 4
        self.cardCount = 0
        random.shuffle(self.shoe)

    def turnCard(self):
        card = self.shoe.pop()
        try:
            val = int(card)
            if val == 10:
                self.cardCount -= 1
            elif val < 7:
                self.cardCount += 1
        except:
            self.cardCount -= 1

        return card


    def shuffle(self):
        random.shuffle(self.shoe)

    def count(self):
        return len(self.shoe)