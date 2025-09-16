class Solution(object):
    def maxNumberOfApples(self, weight):
        total = sum(weight)
        weight.sort(reverse=True)
        i = 0
        while total > 5000 and i<len(weight):
            total -= weight[i]
            i += 1
        
        return len(weight) - i
