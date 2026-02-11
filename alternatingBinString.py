debugMode = True


def FindMinSwaps(s):
    #pidgeonhole

    onesCount = s.count("1")
    halfLen = len(s) / 2
    if abs(onesCount - halfLen) > 1:
        print("NOT POSSIBLE")
        return -1
    if len(s) <= 2:
        return 0

    s = list(s)

    i = 1
    swaps = 0
    while i < len(s):
        #if find dupe
        if s[i] == s[i-1]:  #0101.1:i
            #find next dupe where not match
            for j in range(i, len(s), 1):
                if s[j] == s[j-1] and s[j] != s[i]:
                    temp = s[i]
                    s[i] = s[j]
                    s[j] = temp
                    swaps += 1
                    #set i = j
        i+=1
    print(s)
    return swaps


if __name__ == '__main__':
    print(FindMinSwaps("10010"))
