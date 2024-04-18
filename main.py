import random

class stockMarket:
    def __init__(self):
        '''
        Format for self.stocks dict

        {
            str :{
            sharePrice: float
            marketCap: float
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
        self.inlfation = 0
        self.time = 0


