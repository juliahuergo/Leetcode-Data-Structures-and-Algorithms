from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        def rowandcol(val):
            
            if n % 2 == 0:
                if val%n == 0: 
                    new_row = n - val//n
                    if new_row % 2 == 0:
                        new_col = 0
                    else:
                        new_col = n-1
                else:
                    new_row = n - 1 - val//n
                    if new_row % 2 == 0:
                        new_col = n - val % n 
                    else:
                        new_col = val%n - 1
            else:
                if val%n == 0:
                    new_row = n - val/n
                    if new_row % 2 == 0:
                        new_col = n - 1
                    else:
                        new_col = 0
                else:
                    new_row = n - 1 - val//n
                    if new_row % 2 == 0:
                        new_col = val%n - 1
                    else:
                        new_col = n - val%n
            
            return new_row, new_col
        
        n = len(board)
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n
        
        queue = deque([(n-1, 0, 1, 0)]) #row, col, val, steps
        seen = {(n-1, 0, 1)} #row, col, val
        
        while queue:
            row, col, val, steps = queue.popleft()
            if val == n*n:
                return steps
            
            for i in range(1, 7):
                new_val = min(val + i, n*n)
                new_row, new_col = rowandcol(new_val)
                
                if valid(new_row, new_col) and (new_row, new_col, new_val) not in seen:
                    seen.add((new_row, new_col, new_val))
                    if board[new_row][new_col] != -1:
                        new_val = board[new_row][new_col]
                        new_row, new_col = rowandcol(new_val)
                    queue.append((new_row, new_col, new_val, steps + 1))
        return -1
