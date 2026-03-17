class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if len(nums) == len(set(nums)):
            return len(nums)
        
        nums = sorted(nums)
        used = set()
        prev = float('-inf')
        
        for num in nums:
            newNo = max(prev+1,num-k)
            #print(newNo)
            if newNo <= num + k:
                used.add(newNo)
                prev = newNo

            
           
        


        print(used)
        return len(set(used))