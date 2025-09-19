class Solution(object):
    def splitArray(self, nums, k):
        
        def check(x):
            i = 0
            total = 0
            
            while i < len(nums):
                sumArr = 0
                while i < len(nums) and (sumArr + nums[i]) <= x:
                    sumArr += nums[i]
                    i += 1
                    
                total += 1
            
            return total <= k
        
        
        left = max(nums) #if len(nums) == k
        right = sum(nums) #if k = 1 (we would take them all)
        
        while left <= right:
            mid = (left+right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
