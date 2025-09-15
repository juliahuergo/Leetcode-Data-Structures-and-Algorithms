class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for i in range(len(points)):
            heapq.heappush(heap, (-(points[i][0]**2 + points[i][1]**2), points[i]))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        return [pair[1] for pair in heap]
