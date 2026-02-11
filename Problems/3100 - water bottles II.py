class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        #bottles
        full = numBottles
        empty = 0
        exchangeRate = numExchange

        #finals
        drank = 0 #bottles drank, you thirsty, thirsty boy

        while full > 0:
            #drink()
            drank += full
            empty+= full
            full = 0
            while empty >= exchangeRate:
                #exchange()
                empty -= exchangeRate
                full+=1
                exchangeRate+=1
            #print('full',full,'empty',empty,'exchangeRate',exchangeRate,'drank',drank)

        return drank

        
        
