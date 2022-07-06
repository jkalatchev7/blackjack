import random


class shoe():
    def __init__(self, numDecks):
        self.shoe = ['A','2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K'] * 4 * numDecks
        self.numRem = [4 * numDecks] * 10
        self.numRem[9] = self.numRem[9] * 4
        random.shuffle(self.shoe)

    def turnCard(self):
        card = self.shoe.pop()
        try:
            self.numRem[int(card) - 1] = self.numRem[int(card) - 1] - 1
        except:
            if card == 'A':
                self.numRem[0] = self.numRem[0] - 1
            else:
                self.numRem[9] = self.numRem[9] - 1

        return card


    def shuffle(self):
        random.shuffle(self.shoe)

    def count(self):
        return len(self.shoe)