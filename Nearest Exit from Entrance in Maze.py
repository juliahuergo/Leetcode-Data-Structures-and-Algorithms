class Solution(object):
    def nearestExit(self, maze, entrance):
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."
        
        m = len(maze)
        n = len(maze[0])
        
        seen = {(entrance[0], entrance[1])}
        queue = deque([(entrance[0], entrance[1], 0)])
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        while queue:
            
            row, col, steps = queue.popleft()
            if (row!= entrance[0] or col != entrance[1]) and (row == 0 or col == 0 or row == m-1 or col == n-1):
                return steps
            
            for x, y in directions:
                new_row, new_col = row + x, col + y
                
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps+1))
        
        return -1
