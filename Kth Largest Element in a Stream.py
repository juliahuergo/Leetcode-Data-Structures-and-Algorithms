class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)
        

    def add(self, val):
        
        heapq.heappush(self.nums, val)
        
        while len(self.nums) > self.k:
            heapq.heappop(self.nums) 
            
        return self.nums[0]

