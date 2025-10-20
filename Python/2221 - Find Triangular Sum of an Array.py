class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        #without cheating to use math, the main optimization is just using the same array
        for j in range(len(nums)-1,0,-1):
            for i in range(0, j, 1):
                nums[i] = (nums[i] + nums[i+1])%10
            #nums[i+1] = 'x' #debuggin
            #print(nums)
        return nums[0]
