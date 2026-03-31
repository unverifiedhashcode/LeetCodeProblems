class Solution:
    def smallestNumber(self, n: int) -> int:
        power = 0
        while 2**power <= n:
            power +=1
        return 2**power - 1