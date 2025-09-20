class Solution(object):
    def allPathsSourceTarget(self, graph):
        def backtrack(curr, i):
            if i == len(graph)-1:
                ans.append(curr[:])
                return
            
            for child in graph[i]:
                curr.append(child)
                backtrack(curr, child)
                curr.pop()           
            
            
        ans = []
        backtrack([0], 0)
        return ans
