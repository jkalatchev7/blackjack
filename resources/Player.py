from resources.utils import handTotal
class Player:
    def __init__(self, name="John"):
        self.money = 0
        self.name = name
        self.cardsInHand = []
        self.ante = 0
        self.followsTable = True
        self.lastDecision = " "
        self.doubleOutcomes = {"Win":0, "Loss":0, "Push":0}
        self.insuranceOutcomes = {"Success":0, "Fail":0}

    def reset(self):
        self.cardsInHand = []
        self.ante = 5

    def addCard(self, card):
        self.cardsInHand.append(card)
        return self.cardsInHand

    def outcome(self, dealerHand, cardCount, cardCountResults):  # copy from main
        """
        Takes in the current hand of the dealer and sums the total, then iterates through each hand of player and compares it to dealer's hand.
        Updates player.money according to each hand winning or losing. If given an empty array as a hand, player already got 21 and hand should be skipped.
        Also takes in arguments such as doubleOutcomes, cardCountResults, etc. and updates them based on argument decision and the outcome.
        """
        dealerSum = handTotal(dealerHand)
        for hand in [self.cardsInHand]:  # temp fix
            if hand:  # account for empty hands where player already won
                playerSum = handTotal(hand)
                if (21 > playerSum) and (playerSum > dealerSum or dealerSum > 21):  # player wins!
                    self.money += self.ante
                    if self.lastDecision == "D": self.doubleOutcomes["Win"] += 1
                    cardCountResults[51 + cardCount] += 1
                    return "W"
                elif (21 > playerSum) and (playerSum == dealerSum):  # push
                    if self.lastDecision == "D": self.doubleOutcomes["Push"] += 1
                    return "D"
                else:  # dealer wins
                    self.money -= self.ante
                    if self.lastDecision == "D": self.doubleOutcomes["Loss"] += 1
                    cardCountResults[51 + cardCount] -= 1
                    return "L"