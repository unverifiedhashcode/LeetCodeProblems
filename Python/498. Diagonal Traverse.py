#While this isn't the prettiest solution visually and it's a bit nest heavy, it's O(n) which is much more important for the purpose of this exercise.
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        retList = []
        matSize = len(mat) * len(mat[0])
        yLen = len(mat)-1
        xLen = len(mat[0])-1
        xPos = 0
        yPos = 0
        i = 0
        direction = 'UP'
        while (i < matSize):
            currVal = mat[yPos][xPos]
            print(currVal)
            if direction == 'UP':   #GOING UP!
                if yPos > 0 and xPos < xLen:
                    
                    xPos += 1
                    yPos -= 1
                else: 
                    if xPos != xLen:    #we hit the top before we hit the right side
                        xPos +=1
                    else:               #we hit the right side
                        yPos += 1
                    direction = 'DOWN'
                    print('dirflip at',currVal,'new direction is',direction)

            else:                   #GOING DOWN!
                if xPos > 0 and yPos < yLen: 
                    
                    xPos -= 1
                    yPos += 1
                else:
                    if yPos != yLen:    #we hit the left side before we hit the bottom
                        yPos +=1
                    else:               #we hit the bottom
                        xPos += 1
                    direction = 'UP'
                    print('dirflip at',currVal,'new direction is',direction)
                    


            retList.append(currVal)
            i+=1

        
        
        return retList