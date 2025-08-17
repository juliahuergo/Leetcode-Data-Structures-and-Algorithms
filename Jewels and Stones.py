class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        ans = 0
        for letter in stones:
            if letter in jewels:
                ans += 1
        return ans
