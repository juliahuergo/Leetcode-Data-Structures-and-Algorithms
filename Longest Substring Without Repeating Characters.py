class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        seen = set()
        ans = 0
        
        for i in range(len(s)):
            while(s[i] in seen):
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            ans = max(ans, i-left+1)
        
        return ans
