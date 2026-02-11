#The only challenge here is how much we can optimize
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        plus = 0
        minus = 0
        for currOp in operations:
            if currOp[1] == '+':
                plus +=1
            else:
                minus +=1
        #print(plus,minus)
        return plus - minus
        
