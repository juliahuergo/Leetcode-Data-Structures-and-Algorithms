class Solution(object):
    def connectSticks(self, sticks):
        if len(sticks) == 1:
            return 0
        
        heapq.heapify(sticks)
        
        ans = 0
        
        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            ans += x+y
            heapq.heappush(sticks, x+y)
        
        return ans
