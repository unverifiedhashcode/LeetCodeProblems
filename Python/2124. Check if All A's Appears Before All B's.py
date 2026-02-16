class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for i in range(len(s)):
            if s[i] == 'b':
                b = True
            elif b:
                return False

        return True