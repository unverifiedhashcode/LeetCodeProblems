class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        maxTime = neededTime[0]
        
        for i in range(1,len(colors)):
            if colors[i] == colors[i-1]:
                totalTime += min(maxTime, neededTime[i])
                maxTime = max(maxTime, neededTime[i])
            else:
                maxTime = neededTime[i]
        return totalTime
