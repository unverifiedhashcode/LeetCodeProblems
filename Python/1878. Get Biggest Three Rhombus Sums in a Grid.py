class Solution:
    @staticmethod
    def calcBloomSum(grid, r, c, bloom):
        if bloom == 0:
            return grid[c][r]
        
        total = 0
        #Walk each of the 4 sides, bloom steps each
        #exclude final corner step because we count that by starting at that corner in that side's calculation
        for i in range(bloom):
            total += grid[c - bloom + i][r + i]   #Top corner to Right corner 
            total += grid[c + i][r + bloom - i]   #Right corner to Bottom corner 
            total += grid[c + bloom - i][r - i]   #Bottom corner to Left corner 
            total += grid[c - i][r - bloom + i]   #Left corner to Top corner 
        
        return total

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rowLen = len(grid[0])
        colLen = len(grid)
        rhombusSums = set()

        #rhombus logic
        for rowPos in range(rowLen):
            for colPos in range(colLen):
                bloom = 0
                while rowPos - bloom >= 0 and rowPos + bloom < rowLen and colPos - bloom >= 0 and colPos + bloom < colLen:
                    #print(rowPos, colPos, bloom)
                    #calc bloom sum 
                    bloomSum = Solution.calcBloomSum(grid, rowPos, colPos, bloom)
                    rhombusSums.add(bloomSum)
                    bloom += 1
        
        #filter largest logic
        print(rhombusSums)
        return sorted(list(rhombusSums), reverse=True)[:3]

