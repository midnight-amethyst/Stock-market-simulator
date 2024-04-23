import random
from JsonIO import JsonIO
import matplotlib.pyplot as plt
import os

def clear():
    os.system("clear")

class stockMarket:

    def __init__(self):
        '''
        Format for self.stocks dict

        {
            str :{
            sharePrice: float
            marketCap: outstandingShares * sharePrice
            maxShares: int
            outstandingShares: int
            askingPrice: float
            sharesGoDownRate: float
            previousEventRating: int
            previousBuyPrice: float
            }
        }
        
        '''
        self.stocks = {
            'aaaa': {
                'sharePrice': 1,
                'marketCap': 1,
                'maxShares': 1,
                'outstandingShares': 1,
                'askingPrice': 1,
                'sharesGoDownRate': 0.1,
                'previousEventRating': 5,
                'previousBuyPrice': 1
            }
        }
        self.averageGrowth = 1.102  # Gains 10.2% every year according to bing
        self.inflation = 1  # As a %
        self.previousInflations = [self.inflation]
        self.time = 0
        self.previousTime = [self.time]
        self.dollar = 1

    def setInflation(self):
        temp = random.random() * 0.1
        posOrNeg = random.randint(1, 2)
        posOrNeg = -1 if posOrNeg == 2 else 1
        self.inflation += temp * posOrNeg
        self.previousInflations.append(self.inflation)

    def tickTime(self, ticks=1):
        self.time += ticks
        self.previousTime.append(self.time)

        self.setInflation()
        self.setDollar()

    def setDollar(self):
        self.dollar = 1 / self.inflation


class createBusiness():

    def __init__(self, ticker, sharePrice, marketCap, maxShares,
                 outstandingShares, askingPrice, sharesGoDownRate,
                 previousEventRating, previousBuyPrice):
        self.ticker = ticker
        self.sharePrice = sharePrice
        self.marketCap = marketCap
        self.maxShares = maxShares
        self.outstandingShares = outstandingShares
        self.askingPrice = askingPrice
        self.sharesGoDownRate = sharesGoDownRate
        self.previousEventRating = previousEventRating
        self.previousBuyPrice = previousBuyPrice



# Class for all ui stuff
class ui:
    def __init__(self):
        self.infoUI = 'Time: 0\nInflation: 1%\n'
        self.ui = '''[0] Tick time
[1] Tick time custom
[2] Buy shares
[3] Sell shares
[4] View stocks
[5] View portfolio
[6] Console
[7] Exit

        '''

        self.defaultUI = '''[0] Tick time
[1] Tick time custom
[2] Buy shares
[3] Sell shares
[4] View stocks
[5] View portfolio
[6] Console
[7] Exit

        '''

    def default(self):
        self.ui = self.default
    def updateInfoUI(self):
        self.infoUI = f'{self.time}\n{self.inflation}\n'
    def tickTime(self, time):
        self.time = f'Time: {time}'
        self.updateInfoUI()
    def updateInflation(self, inflation):
        self.inflation = f'Inflation: {inflation * 100}%'
        self.updateInfoUI()
    



market = stockMarket()
UI = ui()
while True:
    clear()
    print(UI.infoUI)
    print(UI.ui)
    value = input()
    if UI.ui == UI.defaultUI:
        if value == '0':
            market.tickTime()
            UI.tickTime(market.time)
        elif value == '1':
            market.tickTime(int(input('How many ticks?\n')))
            UI.tickTime(market.time)
        elif value == '2':
            pass
        elif value == '3':
            pass
        elif value == '4':
            pass
        elif value == '5':
            pass
        elif value == '6':
            pass
        else:
            pass
    input()
    
    
