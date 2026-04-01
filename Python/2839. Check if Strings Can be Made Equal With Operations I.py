class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        l1 = list(s1)
        l2 = list(s2)
        for i in range(len(l1) -2):
            if l1[i] != l2[i]:
                print(l1[i],l2[i],":",l1[i+2])
                if l1[i+2] != l2[i]:
                    return False
                #successful swap warranted
                temp = l1[i]
                l1[i] = l1[i+2]
                l1[i+2] = temp
        #check last 2
        for i in range((len(l1) -2),len(l1)):
            print(i)
            if l1[i] != l2[i]:
                return False
        return True
