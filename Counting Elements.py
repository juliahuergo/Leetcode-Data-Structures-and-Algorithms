class Solution(object):
    def countElements(self, arr):
        arrSet = set(arr)
        count = 0
        for element in arr:
            if element+1 in arrSet:
                count += 1
        return count
        
