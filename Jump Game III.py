class Solution(object):
    def canReach(self, arr, start):
        def neighbours(i):
            ans = []
            if 0 <= i+arr[i] < len(arr):
                ans.append(i+arr[i])
                
            if 0 <= i-arr[i] < len(arr):
                ans.append(i-arr[i])
                
            return ans
            
        
        seen = {start}
        queue = deque([(start)])
        
        while queue:
            
            pos = queue.popleft()
            
            if arr[pos] == 0:
                return True
            
            for node in neighbours(pos):
                if node not in seen:
                    seen.add(node)
                    queue.append(node)      
        
        
        return False
