class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum = total = 0
        for i in range(len(nums)):
            total += nums[i]
            minimum = min(minimum, total)            
        return abs(minimum) + 1
            
        
