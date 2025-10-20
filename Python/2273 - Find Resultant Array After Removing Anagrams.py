def createHashMap(word):
    wordMap = [0] * 26
    for currChar in word:
        wordMap[ord(currChar)-97] +=1
    return wordMap

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        currHash = []
        prevHash = []

        for currWord in words[:]:
            currHash = createHashMap(currWord)
            if currHash == prevHash:
                words.remove(currWord)
            else:
                prevHash = currHash
        return words

        