class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U',]
        vowelsSpotted = []
        vowelLocs = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowelsSpotted.append(s[i])
                vowelLocs.append(i)
        vowelsSpotted.sort()
        sList = list(s)
        for i in range(len(vowelLocs)):
            sList[vowelLocs[i]] = vowelsSpotted[i]
        return "".join(sList)