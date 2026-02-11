class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            elem = nums[i]
            j = -1 #if we get this, things are very bad
            if elem == 0:
                j = i
                #print('=',j)
            else: 
                currSum = i + elem
                arrSize = len(nums)
                j = currSum % arrSize
                #print('+',currSum, arrSize, j)
            res.append(nums[j])
        return res