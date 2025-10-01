debugMode = True


def debugPrint(message):
    if debugMode:
        print(message)


def countIslands(grid):
    if len(grid) <= 0:
        return

    maxY = len(grid) - 1
    maxX = len(grid[0]) - 1

    islands = 0
    yRow = 0
    xCol = 0

    while yRow < maxY+1:
        if yRow == 3:
            print()
        while xCol < maxX+1:
            #we're just going through each value in the grid
            if grid[yRow][xCol] == "1":
                #break 2
                for xColSweep in range(xCol,maxX +1, 1):
                    if grid[yRow][xColSweep] == "1":
                        grid[yRow][xColSweep] = "x"
                        #break 1
                        for yRowSweep in range(yRow+1, maxY + 1, 1):
                            if grid[yRowSweep][xColSweep] == "1":
                                grid[yRowSweep][xColSweep] = "x"
                            else:
                                break #1
                    else:
                        break #2
                #entire island is now swept
                islands +=1
            xCol+=1
        yRow +=1
        xCol = 0

    return islands


def countLoneIslands(grid):
    if len(grid) <= 0:
        return 0

    maxY = len(grid) - 1
    maxX = len(grid[0]) - 1

    islands = 0

    for yRow in range(0,maxY+1):
        for xCol in range(0,maxX+1):
            if grid[yRow][xCol] == "1":
                isValid = True
                #check right (left edge check)
                if xCol != maxX:
                    if grid[yRow][xCol+1] == "1": isValid = False
                #check left (right edge check)
                if xCol != 0 and isValid == True:
                    if grid[yRow][xCol-1] == "1": isValid = False
                #check down (top edge check)
                if yRow != maxY and isValid == True:
                    if grid[yRow + 1][xCol] == "1": isValid = False
                # check up (bottom edge check)
                if yRow != 0 and isValid == True:
                    if grid[yRow - 1][xCol] == "1": isValid = False
                if isValid:
                    islands += 1
    return islands

if __name__ == '__main__':
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","1"],
            ["0","0","0","1","0"]]
    print(countIslands(grid))
