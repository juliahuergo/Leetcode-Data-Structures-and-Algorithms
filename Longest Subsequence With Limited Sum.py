class Solution(object):
    def answerQueries(self, nums, queries):
        
        def binSearch(arr, target):
            left = 0
            right = len(arr) - 1
            
            while left <= right:
                mid = (left+right)//2
                
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return min(left, right)
        
        nums.sort()
        for i in range(1,len(nums)): #nums is now a prefix sum (in ascending order) of the original nums
            nums[i] += nums[i-1]
        
        answer = []
        for i in range(len(queries)):
            answer.append(binSearch(nums, queries[i]) + 1)
        
        return answer
            
