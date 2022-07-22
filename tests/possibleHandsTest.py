from resources.utils import possibleDealerHands


# Method to compute and save the possible hands for each dealer upcard... so we don't have to compute this every time
def possibleDealerHandsCSV():
    possibleDealerHands(['2'])
    possibleDealerHands(['3'])
    possibleDealerHands(['4'])
    possibleDealerHands(['5'])
    possibleDealerHands(['6'])
    possibleDealerHands(['7'])
    possibleDealerHands(['8'])
    possibleDealerHands(['9'])
    possibleDealerHands(['F'])
    possibleDealerHands(['A'])


possibleDealerHandsCSV()
