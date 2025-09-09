class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        numR = len(grid)
        numC = len(grid[0])
        
        def valid(row, col):
            return 0 <= row < numR and 0 <= col < numC and grid[row][col] == 1
        
        def dfs(row, col):
            count = 1
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    count += dfs(new_row, new_col)
            return count
        
        seen = set()
        ans = 0
        
        
        directions = ([-1, 0], [0, 1], [1, 0], [0, -1])
        
        for row in range(numR):
            for col in range(numC):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    ans = max(ans, dfs(row, col))
                    
        return ans
