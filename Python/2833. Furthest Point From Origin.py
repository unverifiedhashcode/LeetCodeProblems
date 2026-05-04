class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        lDisp = 0
        rDisp = 0
        blankDisp = 0
        for item in moves:
            match item:
                case 'L':
                    lDisp += 1
                case 'R':
                    rDisp += 1
                case '_':
                    blankDisp += 1
        return max(lDisp, rDisp) - min(lDisp, rDisp) + blankDisp

        
