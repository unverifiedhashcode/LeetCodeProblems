class Solution:
    def minTimeToType(self, word: str) -> int:
        word = 'a' + word #makes the pointer start at a
        
        wheelLen = 26
        mid = wheelLen / 2

        time = 0

        for wordPos in range(len(word) - 1):
            currLetter = word[wordPos]
            nextLetter = word[wordPos + 1]

            dist  =  abs(ord(nextLetter) - ord(currLetter))
            #print('dist from',currLetter,'to',nextLetter,'is',dist)
            time += min(dist,wheelLen-dist) +1
            
            #print('nt:',time)
            #no need to reassign currLetter, it's taken care of automatically with the loop iteration

        return(time) 


            
