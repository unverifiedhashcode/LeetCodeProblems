class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        countList = Counter(nums)
        oldi = 0
        oldj = 0
        oldNo = 0
        for currNo in sorted(Counter(nums)):
            
            if currNo - oldNo == 1:
                #standard house robber
                bestVal = max(oldj, currNo * countList[currNo] + oldi)
                
            else:
                #just take the best plus whatever was better before
                bestVal = currNo * countList[currNo] + max(oldi, oldj)
            #same regardless
            oldi = oldj
            oldj = bestVal
            oldNo = currNo
        return(max(oldi,oldj))
