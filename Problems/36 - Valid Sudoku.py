debugMode = True

tc1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def clearNine():
    return [0]*9

def printBoard(board): #debuggin
    for row in board:
        print(row)

def isValidSudoku(inputBoard):
    rowCheck = clearNine()
    colCheck = clearNine()
    boxCheck = clearNine()

    #check rows
    for row in range(0,9,1):
        rowCheck = clearNine()
        for rowPos in range(0, 9, 1):B
            currVal = inputBoard[row][rowPos]
            if currVal != '.': #if its actually a number
                mapEq = int(currVal) - 1 #map position equivalent
                #print(mapEq)
                if rowCheck[mapEq] == 0:
                    rowCheck[mapEq] = 1
                else:
                    print('invalid!',inputBoard[row])
                    return -1

    #check columns
    for col in range(0,9,1):
        colCheck = clearNine()
        for colPos in range(0, 9, 1):
            currVal = inputBoard[colPos][col]
            if currVal != '.': #if its actually a number
                mapEq = int(currVal) - 1 #map position equivalent
                #print(mapEq)
                if colCheck[mapEq] == 0:
                    colCheck[mapEq] = 1
                else:
                    print('invalid column number:',col)
                    return -1
    #check boxes
    for boxRow in range(0, 3, 1):
        for boxCol in range(0, 3, 1):
            boxCheck = clearNine()
            #begin inner box scan
            for innerRow in range(0, 3, 1):
                for innerCol in range(0, 3, 1):
                    currVal = inputBoard[3*boxRow + innerRow][3*boxCol + innerCol]
                    #print(currVal)
                    if currVal != '.':  # if its actually a number
                        mapEq = int(currVal) - 1  # map position equivalent
                        # print(mapEq)
                        if boxCheck[mapEq] == 0:
                            boxCheck[mapEq] = 1
                        else:
                            print('invalid box at boxrow:',boxRow,'boxCol:',boxCol )
                            printBoard(inputBoard)
                            return -1
    return 1


isValidSudoku(tc1)