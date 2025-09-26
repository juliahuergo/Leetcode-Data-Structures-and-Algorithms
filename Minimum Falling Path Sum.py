class Solution(object):
    def minFallingPathSum(self, matrix):
        def dp(row, col):
            if row == 0:
                return matrix[row][col]
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            ans = float("inf")
            if row > 0:
                if col < n-1:
                    ans = min(ans, dp(row-1, col+1))
                if col > 0:
                    ans = min(ans, dp(row-1, col-1))
                    
                ans = min(ans, dp(row-1, col))
            
            ans += matrix[row][col]
            
            memo[(row, col)] = ans
            return ans            
            
            
        memo = {}
        m = len(matrix)
        n = len(matrix[0])
        
        return min(dp(m-1, col) for col in range(n))
