class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        colLen = len(grid)
        rowLen = len(grid[0])
        #make tuple arr of min, max initialzed to None, None
        minMaxArr = [[(None, None)] * rowLen for _ in range(colLen)]
        minMaxArr[0][0] = (grid[0][0], grid[0][0])
        

        #top row and left col exceptions built in to save n-1*n-1 if statements

        #do top row
        for i in range(1,rowLen):
            minMaxArr[0][i] = (minMaxArr[0][i-1][0] * grid[0][i], minMaxArr[0][i-1][0]* grid[0][i])

        #do left col
        for i in range(1,colLen):
            minMaxArr[i][0] = (minMaxArr[i-1][0][0] * grid[i][0], minMaxArr[i-1][0][0] * grid[i][0])
        
        #print(minMaxArr)
        compArr = [0,0,0,0]
        for currCol in range(1,colLen):
            for currRow in range(1,rowLen):
                #print(grid[currCol][currRow],minMaxArr[currCol-1][currRow][0])
                compArr[0] = grid[currCol][currRow] * minMaxArr[currCol-1][currRow][0]
                compArr[1] = grid[currCol][currRow] * minMaxArr[currCol-1][currRow][1]

                compArr[2] = grid[currCol][currRow] * minMaxArr[currCol][currRow-1][0]
                compArr[3] = grid[currCol][currRow] * minMaxArr[currCol][currRow-1][1]

                minMaxArr[currCol][currRow] = (min(compArr),max(compArr))
        
        #print(minMaxArr)
        #print(minMaxArr[colLen-1][rowLen-1])
        maxVal = max(minMaxArr[colLen-1][rowLen-1])
        if maxVal >= 0:
            return maxVal % (10**9 + 7)
        return -1
