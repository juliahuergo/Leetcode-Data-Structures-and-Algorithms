class Solution(object):
    def minStoneSum(self, piles, k):
        heap = [-num for num in piles]
        heapq.heapify(heap)
        
        for i in range(k):
            num = heapq.heappop(heap)
            heapq.heappush(heap, math.floor(-num/2)+num)
            
        return int(-sum(heap))
        
