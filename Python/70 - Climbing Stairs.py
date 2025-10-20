class Solution:
    def climbStairs(self, n: int) -> int:
        stepi = 0
        stepj = 1
        for i in range(n):
            y = stepi + stepj
            stepi = stepj
            stepj = y
        return y
        
