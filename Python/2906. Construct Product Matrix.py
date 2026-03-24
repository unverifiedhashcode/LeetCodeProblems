class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        #get a list of all the products of each row
        rowProducts = []
        for row in grid:
            currRowProd = 1
            for item in row:
                item = item % 12345
                if item != 0:
                    currRowProd *= item
            rowProducts.append(currRowProd)
        #make final prod (unsure)
        totalProd = 1
        for item in rowProducts:
            totalProd *= item
        #might modulo 12345 here

        #make final
        retArr = [] #can be made faster by not constantly appending
        for rowi in grid:
            currRow = []
            for itemi in rowi:
                if itemi == 0:
                    currRow.append(0)
                else:
                    currRow.append((totalProd // itemi) % 12345)
            retArr.append(currRow)

        return retArr
