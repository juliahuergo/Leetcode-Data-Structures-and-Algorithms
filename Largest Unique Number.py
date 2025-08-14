class Solution(object):
    def largestUniqueNumber(self, nums):
        counts = Counter(nums)
        right = max(counts.keys())
        while right >= 0:
            if counts[right] == 1:
                return right
            right -= 1
        return -1
