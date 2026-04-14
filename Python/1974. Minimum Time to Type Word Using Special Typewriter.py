class Solution:
    def minTimeToType(self, word: str) -> int:
        word = 'a' + word #makes the pointer start at a
        
        wheelLen = 26
        mid = wheelLen / 2
        wheelPos = 0

        time = 0

        for wordPos in range(len(word) - 1):
            currLetter = word[wordPos]
            nextLetter = word[wordPos + 1]

            dist  =  ord(nextLetter) - ord(currLetter)
            print('dist from',currLetter,'to',nextLetter,'is',dist)
            if dist >= 0: #dist pos
                if dist > mid:
                    time += (wheelLen - dist)
                    print('PR')
                else:
                    time += dist
                    print('PL')
                time +=1
                
            else: #dist neg
                dist*=-1
                if dist < mid:
                    time += dist
                    print('NL')
                else:
                    time += (wheelLen - dist)
                    print('NR')
                time +=1
            print('nt:',time)
            #no need to reassign currLetter, it's taken care of automatically with the loop iteration

        return(time) 


            
