class Solution:
    def createCustomHashes(self, s1):
        #even hashmap
        evenHash = [0] * 26
        for i in range(0,len(s1),2):
            currChar = s1[i]
            #print(currChar)
            evenHash[ord(currChar)-97] +=1
            #print(evenHash)
        
        oddHash = [0] * 26
        for i in range(1,len(s1),2):
            currChar = s1[i]
            oddHash[ord(currChar)-97] +=1
            
        return [evenHash, oddHash]

    def checkStrings(self, s1: str, s2: str) -> bool:
        [s1even,s1odd] = self.createCustomHashes(s1)
        [s2even,s2odd] = self.createCustomHashes(s2)

        #print(s1even, s2even)
        if s1even == s2even and s1odd == s2odd:
            return True
        return False
