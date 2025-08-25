class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        stack = []
        prevAns = defaultdict(lambda: -1)
        
        for i in range(len(nums2)): #index matched to next greater number
            while stack and nums2[i] > nums2[stack[-1]]: #max len(nums2) iterations in total 
                j = stack.pop()
                prevAns[nums2[j]] = nums2[i]
            stack.append(i) #O(1) operation (using a stack)
            #O(len((nums2)) bc inner loop is amortized O(1)
        
        ans = []
        for i in range(len(nums1)): #each number in nums1 matched to its greater number
            ans.append(prevAns[nums1[i]]) #O(1) operation
            #O(len(nums1)) 
        
        return ans 

    #TOTAL COMPLEXITY = O(LEN(NUMS2) + LEN(NUMS1))
