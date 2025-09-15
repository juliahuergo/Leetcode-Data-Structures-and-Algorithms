class Solution(object):
    def findKthLargest(self, nums, k):
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        while k > 1:
            k -= 1
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)
