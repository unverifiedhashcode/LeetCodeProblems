class Solution:
    def smallestNumber(self, n: int) -> int:
        prev = 1
        curr = 2
        while curr <= n:
            prev = curr
            curr *= 2
        return curr - 1
            