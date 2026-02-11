class Solution:
    #TIL to use a set instead of a list.
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        nLen = 1
        remainders = set()
        remainder = 0
        while remainder not in remainders:
            remainders.add(remainder) #sets use add instead of append
            #print(remainders)
            remainder = n % k
            if remainder == 0:
                return nLen
            else:
                nLen += 1
                n = (n * 10) + 1
        return -1 
        