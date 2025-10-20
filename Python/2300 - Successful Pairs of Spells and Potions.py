def roundUp(number):
    if number == int(number):
        #print('rounded ',number,' to ',int(number))
        return int(number)
    else:
        #print('rounded ',number,' to ',int(number)+1)
        return (int(number) + 1)

def binarySort(arr): #abandoned for pythons faster built in timsort
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid
        arr[left + 1:i + 1] = arr[left:i]
        arr[left] = key
    return arr


def binarySearch(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left  # index of first element >= target

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        minStren = success
        res = []
        potions.sort()
        for s in spells:
            successes = 0 #successful enough to hit critera
            minPotency = roundUp(minStren / s)
            #print('====')
            #print('minPotency',minPotency)
            minPos = binarySearch(potions,minPotency)
            successes = len(potions) - minPos  
            #print('::',len(potions),minPos)
            res.append(successes)
        return res
