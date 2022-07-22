import numpy as np
import pandas as pd
from resources import Shoe, model

a  = np.array([
 ['H','H','D','D','D','D','H','H','H','H'],
 ['H','H','D','D','D','D','H','H','H','H'],
 ['H','H','D','D','D','D','H','H','H','H'],
 ['H','H','D','D','D','D','H','H','H','H'],
 ['H','D','D','D','D','D','H','H','H','H'],
 ['H','D','D','D','D','D','S','S','H','H'],
 ['S','S','S','S','S','D','S','S','S','S'],
 ['S','S','S','S','S','S','S','S','S','S']])

df = pd.DataFrame(a, index=['A,2', 'A,3','A,4','A,5','A,6', 'A,7','A,8', 'A,9'] ,columns = ['A','2','3', '4', '5', '6', '7', '8', '9', '10'])

# s = shoe(5)
# dealerOdds = model.updatedDealerOdds(s, ['8'])
# model.hitWinOdds(dealerOdds, ['A', '4'], s, " ")
# dealerOdds = model.updatedDealerOdds(s, ['9'])
# model.hitWinOdds(dealerOdds, ['A', '4'], s, " ")
# dealerOdds = model.updatedDealerOdds(s, ['10'])
# model.hitWinOdds(dealerOdds, ['A', '4'], s, " ")
# dealerOdds = model.updatedDealerOdds(s, ['A'])
# model.hitWinOdds(dealerOdds, ['A', '4'], s, " ")

b = np.array([['H','H','H','H','D','D','H','H','H','H'],
 ['H','D','D','D','D','D','D','H','H','H'],
 ['H','D','D','D','D','D','D','D','D','H'],
 ['H','D','D','D','D','D','D','D','D','D'],
 ['H','H','H','S','S','S','H','H','H','H'],
 ['H','S','S','S','S','S','H','H','H','H'],
 ['H','S','S','S','S','S','H','H','H','H'],
 ['H','S','S','S','S','S','H','H','H','H'],
 ['H','S','S','S','S','S','H','H','H','H']])

dfB = pd.DataFrame(b, index = ['8','9','10','11','12','13','14','15','16'], columns = ['A','2','3', '4', '5', '6', '7', '8', '9', '10'])
print(dfB)


s = Shoe(5)
dealerOdds = model.calc_dealerOdds(s, ['A'])
model.hitWinOdds(dealerOdds, ['2', '3'], s, " ")
model.hitWinOdds(dealerOdds, ['2', '4'], s, " ")
model.hitWinOdds(dealerOdds, ['2', '5'], s, " ")
model.hitWinOdds(dealerOdds, ['2', '6'], s, " ")
model.hitWinOdds(dealerOdds, ['2', '7'], s, " ")
model.hitWinOdds(dealerOdds, ['2', '8'], s, " ")
model.hitWinOdds(dealerOdds, ['2', '9'], s, " ")
model.hitWinOdds(dealerOdds, ['2', '10'], s, " ")
model.hitWinOdds(dealerOdds, ['3', '10'], s, " ")
model.hitWinOdds(dealerOdds, ['4', '10'], s, " ")
model.hitWinOdds(dealerOdds, ['5', '10'], s, " ")
model.hitWinOdds(dealerOdds, ['6', '10'], s, " ")
model.hitWinOdds(dealerOdds, ['7', '10'], s, " ")
model.hitWinOdds(dealerOdds, ['8', '10'], s, " ")
model.hitWinOdds(dealerOdds, ['9', '10'], s, " ")
model.hitWinOdds(dealerOdds, ['10', '10'], s, " ")