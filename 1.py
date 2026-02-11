class Solution(object):
    def kthCharacter(self, k):
        return self.helper(k)

    def helper(self, k):
        # Base case
        if k == 1:
            return 'a'

        # Find largest power of 2 <= k
        length = 1
        while length * 2 < k:
            length *= 2

        # k is in the right half if > length
        if k <= length:
            return self.helper(k)              # left half, same value
        else:
            ch = self.helper(k - length)       # recurse into left half
            return chr(ord(ch) + 1)    