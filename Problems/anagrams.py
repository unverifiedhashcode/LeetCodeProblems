case1 = ["eat","tea","tan","ate","nat","bat"]
case2 = ["ac","c"]

def createWordCountDict(word):
    #abandoned because dictionaries are SLOW compared to fixed lists
    wordDict = {}
    for char in word:
        if char in wordDict:
            wordDict[char] = wordDict[char] + 1
        else:
            wordDict[char] = 1
    return wordDict

def createLetterCountTuple(word):
    letList = [0] * 26
    for currChar in word:
        placeLoc = ord(currChar) - 97
        letList[placeLoc] = letList[placeLoc] + 1
    letList = tuple(letList)
    print('letterlist for ',word,':',letList)
    return letList

def anagramGrouper(inputs):
    allWordDicts = {}
    for currWord in inputs:
        currWordKey = createLetterCountTuple(currWord)
        allWordDicts.setdefault(currWordKey,[]).append(currWord)
    print(allWordDicts.values())
    print(list(allWordDicts.values()))

def FancyanagramGrouper(inputs):
    allWordDicts = {}
    for word in inputs:
        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord('a')] += 1
        key = tuple(counts)
        allWordDicts.setdefault(key, []).append(word)
    return list(allWordDicts.values())

if __name__ == '__main__':
    anagramGrouper(case1)
    FancyanagramGrouper(case2)
