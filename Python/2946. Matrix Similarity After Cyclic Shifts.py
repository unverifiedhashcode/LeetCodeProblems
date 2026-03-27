class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rowLen = len(mat[0])
        rightShift = k % rowLen
        leftShift = rowLen - rightShift

        #just iterate through row. Start with the right shift
        referencePos = 0

        isOdd = True
        for row in mat:
            if isOdd:
            #check right shift
                for i in range(rowLen):
                    shiftPos = (i + rightShift) % rowLen
                    if (row[i] != row[shiftPos]):
                        return False
            else: #isEven
            #check left shift
                #print('L')
                for i in range(rowLen-1,0,-1):
                    #print(row[i], row[shiftPos])
                    shiftPos = (i + leftShift) % rowLen
                    if (row[i] != row[shiftPos]):
                        #print('error! returning false')
                        return False
            isOdd = not isOdd
        
        return True
