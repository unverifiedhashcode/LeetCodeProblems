valIps = []
#SHIT
def checkRootValid(root):
    if root == '0':
        return True
    if int(root)>255:
        return False
    if str(int(root)) != root: #'001' would become 1, which would become '1'
        return False
    return True

def isValid(root,remains,remainingBlocks): #s will be the truncated string by blocks
    strLen = len(remains)
    if remainingBlocks == 0:
        print('no remaining blocks',root)
        if root not in valIps:
            valIps.append((root))
        return
    if remainingBlocks > strLen or remainingBlocks * 3 < strLen or strLen == 0:
        #print('too long or too short!')
        return
    else:
        print(remainingBlocks,'<',strLen,'<',remainingBlocks * 3)
    if remainingBlocks < 1:
        return
    #now get a block of 3
    for i in range(1,4,1):
        newRoot = remains[0:i]
        newRemains = remains[i:len(remains)]
        #print('root:',root,'rem:',remains,'blocks remaining:',remainingBlocks)
        if checkRootValid(newRoot):
            recurRoot = ''
            if root == '':
                recurRoot = newRoot
            else:
                recurRoot = root + '.' + newRoot
            isValid(recurRoot,newRemains,remainingBlocks-1)
        else:
            print('invalid root:',newRoot)

#GOOD


def checkValid(block):
    #no leading zeroes unless its just zero
    if block[0] == '0' and len(block) > 1:
        return False
    if int(block)>255:
        return False
    return True

def SolveIt(s,currPos, createdIP):
    if len(createdIP) == 4:
        if currPos == len(s):
            return [".".join(createdIP)]
        return []

    results= []
    remainingChars = len(s) - currPos
    remainingBlocks = 4 - len(createdIP)
    if remainingChars < remainingBlocks or remainingChars > remainingBlocks * 3:
        return []

    for size in range(1,4,1):
        amendedPos = currPos + size
        if amendedPos > len(s):
            break
        currBlock = s[currPos:amendedPos]
        if checkValid(currBlock):
            results.extend((SolveIt(s,amendedPos,createdIP + [currBlock])))
    return results

def restoreIpAddresses(s: str):
    return SolveIt(s,0,[])


print(restoreIpAddresses("101023"))