class Solution(object):
    def smallestDivisor(self, nums, threshold):
        
        def check(n):
            total = 0
            
            for num in nums:
                total += (num + n - 1) // n
                
            return total <= threshold
        
        left = 1
        right = max(nums)
        
        while left <= right:
            mid = (left+right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
            
        
