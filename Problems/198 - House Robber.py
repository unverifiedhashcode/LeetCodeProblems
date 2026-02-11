
########################
#           x
#   0   0   1   2   3   2   3   10  7   2
#   0   0<--1<--2<--4<--4<--7   14  15  16
#  oldi oldj y


class Solution:
    def rob(self, nums: List[int]) -> int:
        oldi = 0
        oldj = 0
        for i in nums: #i is current house val
            x = i + oldi #x is oportunity cost of robbing current house and the house 2 back (and its max combo)
            y = max(x,oldj) # is which is better: to rob this house and skip the prev or just skip this house because the prev is that much better 
            oldi = oldj #iterate
            oldj = y    #iterate
        return max(oldi, oldj)
