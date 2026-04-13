class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        textLen = len(encodedText)
        cols = len(encodedText) / rows
        rowNo = 0
        colNo = 0
        sol = ''
        currPos = 0

        lastRow = 0
        lastCol = 0

        while lastCol < cols:
            #print(rowNo, colNo)
            #print(currPos,encodedText[currPos])
            sol += encodedText[currPos]

            rowNo += 1
            colNo += 1
            if colNo > cols or rowNo >= rows:
                
                lastCol +=1
                colNo = lastCol
                rowNo = 0

            currPos = int(colNo + (rowNo * cols))
            if currPos >= textLen:
                break
            


        return "".join(sol).rstrip()

            
        
