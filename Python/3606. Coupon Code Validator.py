import bisect

def isValidChars(inpStr):
    inpStr = inpStr.replace('_','x')
    if inpStr.isalnum():
        return True
    return False 

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validCategories = ["electronics", "grocery", "pharmacy", "restaurant"]

        acceptedCode = []
        acceptedCategory = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in validCategories and isValidChars(code[i]):
                acceptedCode.append(code[i])
                acceptedCategory.append(businessLine[i])

        sortedCodeCat = sorted(zip(acceptedCategory,acceptedCode))
        finalResult = []
        for code in sortedCodeCat:
            finalResult.append(code[1])
        return finalResult
