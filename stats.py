# File that calculates probablities of verious occurences
from dealer import dealer
from utils import *
def dealer_likelihoods(dealer, shoe):
    dealerCards = dealer.cardsInHand
    dealerFirst = dealerCards[0]

    oddsArr = [0] * 21

    val = hand(dealerFirst)

    shoe.prob()