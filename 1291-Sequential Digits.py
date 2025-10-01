debugMode = True
import math

def generateSeq(startNo, maxPow):
    print('gs w ',startNo,maxPow)
    seqNo = 0
    for currPow in range(0,maxPow,1):
        addNo = (startNo + currPow) * pow(10,maxPow-currPow-1)
        seqNo = seqNo + addNo

    return seqNo

def getPow10(number):
    print('power:',math.floor(math.log10(number)))
    return math.floor(math.log10(number))

def sequentialDigits(low, high):
    finAnswer = []

    for powMult in range(getPow10(low),getPow10(high)+2,1):
        print(powMult)
        for startNo in range(1,9-powMult+2,1):
            currNo = generateSeq(startNo,powMult)
            print('currNo',currNo)
            if currNo >= low and currNo <= high:
                finAnswer.append(currNo)
    print(finAnswer)


sequentialDigits(234,2314)