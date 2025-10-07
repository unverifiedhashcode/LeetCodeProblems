def addBinDigits3(a,b,c):
    #these would all be made by the compiler in stack anyway if I did it all in one statement
    a = int(a)
    b = int(b)
    c = int(c)
    res = a + b + c
    if res == 0:
        return ['0','0']
    if res == 1:
        return ['1','0']
    if res == 2:
        return ['0','1']
    if res == 3:
        return ['1','1']


    
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #make both the same length
        a = a.zfill(len(b))
        b = b.zfill(len(a))

        a = '0' + a
        b = '0' + b

        #print(a,b)
        #inits
        ans = ''
        ansDig = '0'
        cDig = '0' #carryoverdig
        for i in range(len(a)-1,-1,-1):
            [ansDig,cDig] = addBinDigits3(a[i],b[i],cDig)
            ans = ansDig + ans
        return str(int(ans))
            