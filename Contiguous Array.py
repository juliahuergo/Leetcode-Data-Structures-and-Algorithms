class Solution(object):
    def findMaxLength(self, nums):
        if len(nums) == 1:
            return 0
        
        prefix = defaultdict(list)
        
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1
            prefix[curr].append(i+1)
        #prefix holds the indices of each possible value of curr, to see which indices have the same value
        
        ans = 0
        for curr in prefix:
            if curr != 0:
                ans = max(ans, max(prefix[curr])-min(prefix[curr])) 
            else:
                ans = max(ans, max(prefix[curr]))
        
        return ans 
