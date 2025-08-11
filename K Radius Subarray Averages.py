class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = []
        if len(nums) == 1 and k==0:
            avgs.append(nums[0])
        
        else:        
            
            for i in range(1, len(nums)): #O(n) complexity
                nums[i] += nums[i-1]

            for i in range(len(nums)):
                if i < k or i >= (len(nums) - k):
                    avgs.append(-1)
                else:
                    total = nums[i+k]
                    if i-k != 0:
                        total -= nums[i-k-1]
                    avgs.append(total//(2*k+1))
        
        return avgs   
