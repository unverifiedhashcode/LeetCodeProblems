class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        hScore = 0
        vScore = 0

        for move in moves:
            match move:
                case 'U':
                    vScore +=1
                case 'D':
                    vScore -=1
                case 'L':
                    hScore +=1
                case 'R':
                    hScore -=1
        
        if hScore == 0 and vScore == 0:
            return True
        return False
        
