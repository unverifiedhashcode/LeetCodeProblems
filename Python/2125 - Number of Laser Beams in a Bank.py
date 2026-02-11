class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        currRow = 0
        prevRow = 0
        totalLasers = 0

        for row in bank:
            deviceCount = row.count('1')
            if deviceCount > 0:
                prevRow = currRow
                currRow = deviceCount
                totalLasers += (prevRow * currRow)
        return totalLasers
