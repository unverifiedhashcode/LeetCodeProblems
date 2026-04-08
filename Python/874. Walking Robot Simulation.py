class Solution:
    def rotate(self, currDir, nextDir):
        
        if nextDir == -1: #right turn
            if currDir == 'N':
                return 'E'
            elif currDir == 'E':
                return 'S'
            elif currDir == 'S':
                return 'W'
            elif currDir == 'W':
                return 'N'
        elif nextDir == -2: #left turn
            if currDir == 'N':
                return 'W'
            elif currDir == 'W':
                return 'S'
            elif currDir == 'S':
                return 'E'
            elif currDir == 'E':
                return 'N'
        print('INVALID DIRECTION INPUTTED')
        return('X')

    def moveForward(self, amt, currPos, dir, obstacles):
        #multiple for loops would messier but faster
        #optimize by adding a check if it moved at all before recalculating max dist
        disp = 0
        nextPos = [0,0]

        for i in range(amt):
            match dir:
                case 'N':
                    nextPos = [currPos[0],currPos[1]+1]
                case 'S':
                    nextPos = [currPos[0],currPos[1]-1]
                case 'E':
                    nextPos = [currPos[0]+1,currPos[1]]
                case 'W':
                    nextPos = [currPos[0]-1,currPos[1]]
            if tuple(nextPos) in obstacles:
                return currPos
            currPos = nextPos
            
        return currPos      
                    
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Instead of: obstacle_set = set(obstacles)
        obstacleSet = {(o[0], o[1]) for o in obstacles}
        #-2 = left turn
        #-1 = right turn
        dir = 'N' #optimize by making a number and making an equation for movement. unnecessary for now
        currPos = [0,0]
        maxDisp = 0

        for command in commands:
            if command == -1 or command == -2:
                dir = self.rotate(dir, command)
                #print('new dir:',dir)
            else:
                currPos = self.moveForward(command, currPos, dir, obstacleSet)
                
                currDisp = (currPos[0]*currPos[0] + currPos[1]*currPos[1])
                #print(currPos,currDisp)
                if currDisp > maxDisp:
                    maxDisp = currDisp
        return maxDisp
        
