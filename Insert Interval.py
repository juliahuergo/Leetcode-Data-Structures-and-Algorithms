class Solution(object):
    def insert(self, intervals, newInterval):
        ans = []
        if len(intervals) == 0:
            ans.append(newInterval)
            return ans
        
        start, end = newInterval
        
        i = 0
        while i < len(intervals) and intervals[i][1] < start:
            ans.append(intervals[i])
            i += 1
            
        while i < len(intervals) and end >= intervals[i][0]:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        ans.append([start, end])
        
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        
                
        return ans             
            
            
                
        
