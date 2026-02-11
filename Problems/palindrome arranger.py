def MinSwaps(s):
    if len(s) <= 2:
        return 0
    pL = 0
    pR = len(s) - 1
    isOdd = len(s) % 2
    #determine when to stop the left of when it should be sorted if it reaches that point
    if isOdd == 1:
        stopPoint = int(len(s)/2) - 1
    else:
        stopPoint = int(len(s)/2)

    swaps = 0
#!!!add edge case
    for pL in range(0,stopPoint, 1):
        if s[pL] != s[pR]:
            tpR = pR #temporary pR
            print(s)
            print(s[:pL + 1] + '=' + s[tpR + 1:pR + 1] + '=' + s[tpR] + '=' + s[pR + 1:len(s)])
            while s[pL] != s[tpR]:

                if pL >= tpR:
                    return -1
                tpR -=1
            #at this s[pL] == s[tpR]
            s = s[:pL+1] + s[tpR + 1:pR+1] + s[tpR] + s[pR+1:len(s) #this causes a problem because it bumps the word around which messes with pR
            print('!'+s)
            swaps += (pR - tpR)
            pR -= 1

    return swaps


if __name__ == '__main__':
    print(MinSwaps('leetlt'))
