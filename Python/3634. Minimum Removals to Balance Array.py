class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        minPos = 0
        maxSize = 0
        for maxPos in range(len(nums)):
            
            while nums[maxPos] > nums[minPos]*k: #unbalanced
                minPos += 1
            #done making it balanced
            
            currSize = (maxPos - minPos) 
            maxSize = max(currSize,maxSize)
            
        
        return len(nums) -1 - maxSize
        
        