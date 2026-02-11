class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 0
        l = 0
        r = 1
        while r < len(prices):
            #print('comparing',prices[r-1],prices[r])
            if prices[r-1] - prices[r] != 1:
                l = r
            else: #descending sequence   
                addNo = (r - l) 
                total += addNo
                #print('!',addNo)
            r += 1
            #print(total)
        return total + len(prices)

