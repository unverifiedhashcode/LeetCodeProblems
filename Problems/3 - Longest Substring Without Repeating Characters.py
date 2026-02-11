
minAscii = 0
maxAscii = 127

def charToInt(c):
    return ord(c)-minAscii

def getHMval(hm,c):
    return hm[charToInt(c)]

def increaseHM(hm, c):
    temp = hm[charToInt(c)]
    hm[charToInt(c)] = temp + 1
    #print(hm)
    return hm

def decreaseHM(hm, c):
    temp = hm[charToInt(c)]
    hm[charToInt(c)] = temp - 1
    #print(hm)
    return hm

class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        #boring inits
        currCharsMap = [0]*(maxAscii-minAscii) #char range
        a = 0
        longestWord = ''
        for b in range(0,len(s),1):
            #print('|a:', a, s[a], '|b:', b, s[b], '||', s)
            currCharsMap = increaseHM(currCharsMap, s[b])  # update in hashmap
            if getHMval(currCharsMap,s[b]) == 1: #valid in hm
                if b - a > len(longestWord) - 1:  # update longest word if necessary
                    longestWord = s[a:b + 1]
                    #print('update lw to', longestWord)
            else:
                while getHMval(currCharsMap,s[b]) > 1 and a<=b:
                    #print('upping a')
                    currCharsMap = decreaseHM(currCharsMap,s[a])
                    a+=1
                    #print('>a:', a, s[a], '!b:', b, s[b])




        print(longestWord)
        return(len(longestWord))