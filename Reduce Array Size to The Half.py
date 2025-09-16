class Solution(object):
    def minSetSize(self, arr):
        
        counts = Counter(arr)
        ordered = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        
        if len(ordered) == 1:
            return 1
        
        removed = 0
        size = len(arr)
        
        i = 0
        while size > len(arr)/2 and i < len(ordered):
            removed += 1
            size -= ordered[i][1]
            i += 1
        
        return removed
