import numpy as np

class Solution:
    def findMidPoint(self, arr) -> bool:
        right = sum(arr)
        left = 0
        for i in arr:
            #print(left,right)
            if left == right:
                return True
            left += i
            right -= i
        return False

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rowLen = len(grid[0])
        colLen = len(grid)
        
        colSums = np.zeros(rowLen)
        rowSums = np.zeros(colLen)
        print(colSums,rowSums)

        #make row/col sums
        for rowNo in range(colLen):
            rowSum = 0
            
            for colNo in range(rowLen):
                
                curr = grid[rowNo] [colNo]
                colSums[colNo] += curr
                rowSum += curr
                #print("r",rowNo,"c",colNo,"Curr",curr)
            #print(colSums)
            rowSums[rowNo] += rowSum

        #print(colSums)
        #print(rowSums)

        #see if midpoint exists
        if self.findMidPoint(rowSums) or self.findMidPoint(colSums):
            return True
        return False

        
        {\rtf1}
