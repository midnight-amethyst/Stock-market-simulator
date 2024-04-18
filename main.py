import random

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
            }
        }
        
        '''
        self.stocks = {}
        self.averageGrowth = 1.102 # Gains 10.2% every year according to bing
        self.inflation = 0
        self.time = 0

    def setInflation(self):
        temp = random.random()
        posOrNeg = random.randint(1, 2)
        posOrNeg = -1 if posOrNeg == 2 else 1
        self.inflation += temp * posOrNeg


market = stockMarket()



