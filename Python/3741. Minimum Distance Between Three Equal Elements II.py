class Solution:

    def minimumDistance(self, nums: List[int]) -> int:
        hash = {}

        #create hash table
        for i in range(len(nums)):
            currVal = nums[i]
            if currVal not in hash:
                hash[currVal] = [i]
            else:
                hash[currVal].append(i)
        
        #do actual problem logic
        minDist = float('inf')
        for currKey in hash:
            if len(hash[currKey]) >= 3:
                #rolling 3 part tracker
                vals = hash[currKey]
                for j in range(len(vals)-2):
                    a = vals[j]
                    b = vals[j+1]
                    c = vals[j+2]
                    #print(a,b,c)
                    currDist = (b-a) + (c - b) + (c - a)
                    if currDist < minDist:
                        minDist = currDist
                    
        #print(hash)
        if minDist == float('inf'):
            return -1
        return(minDist)
        
