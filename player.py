from utils import hand

class player:
    def __init__(self):
        self.money = 0
        self.cardsInHand = []
        self.ante = 0

    def reset(self):
        self.cardsInHand = []
        self.ante = 5

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

    def addCard(self, card):
        self.cardsInHand.append(card)
        return self.cardsInHand

    def outcome(self, dealerHand, decision, doubleOutcomes, cardCount, cardCountResults):  # copy from main
        """
        Takes in the current hand of the dealer and sums the total, then iterates through each hand of player and compares it to dealer's hand.
        Updates player.money according to each hand winning or losing. If given an empty array as a hand, player already got 21 and hand should be skipped.
        Also takes in arguments such as doubleOutcomes, cardCountResults, etc. and updates them based on argument decision and the outcome.
        """
        dealerSum = hand(dealerHand)
        for hand in self.cardsInHand:
            if hand:  # account for empty hands where player already won
                playerSum = hand(hand)
                if (21 > playerSum) and (playerSum > dealerSum or dealerSum > 21):  # player wins!
                    self.money += self.ante
                    if decision == "D": doubleOutcomes["Win"] += 1
                    cardCountResults[51 + cardCount] += 1
                elif (21 > playerSum) and (playerSum == dealerSum):  # push
                    if decision == "D": doubleOutcomes["Push"] += 1
                    pass
                else:  # dealer wins
                    self.money -= self.ante
                    if decision == "D": doubleOutcomes["Loss"] += 1
                    cardCountResults[51 + cardCount] -= 1