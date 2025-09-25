class Solution(object):
    def maxProfit(self, prices, fee):
        def dp(i, holding):
            if i == len(prices):
                return 0
            
            if (i+1, holding) in memo:
                return memo[(i+1, holding)]
            
            ans = dp(i+1, holding)
            
            if holding:
                ans = max(ans, prices[i] + dp(i+1, False))
            else:
                ans = max(ans, -prices[i] -fee + dp(i+1, True))
            
            memo[(i+1, holding)] = ans 
            return ans
        
        memo = {}
        
        return dp(0, False) 
                
