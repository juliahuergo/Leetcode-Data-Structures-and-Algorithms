class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr = 0
        ans = 0
        right = left = 0
        
        while(right < len(nums)):
            if(nums[right] == 0):
                curr += 1
            
            while(curr > k):
                if(nums[left] == 0):
                    curr -= 1
                left += 1
            
            ans = max(ans, right-left+1)
            right += 1
        
        return ans 
                
