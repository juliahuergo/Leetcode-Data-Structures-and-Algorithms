class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        
        if n == 1:
            return cost[0]
        
        dp = [0]*(n+1)
        
        dp[n] = 0
        dp[n-1] = cost[-1]
        
        for i in range(n-2, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i] 
            
        
        return min(dp[0], dp[1])
