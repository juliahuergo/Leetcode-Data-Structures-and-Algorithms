class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        def dp(row, col):
            if obstacleGrid[row][col] == 1:
                return 0
                
            if row+col == 0:
                return 1
            
            if (row, col) in memo:
                return memo[(row,col)]
            
            ans = 0
            if row > 0:
                ans += dp(row-1, col)
            if col > 0:
                ans += dp(row, col-1)
            
            memo[(row, col)] = ans
            return ans
            
            
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return dp(m-1, n-1)
