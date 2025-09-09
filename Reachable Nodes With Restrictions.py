class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = {0}
        for node in restricted:
            visited.add(node)
            
        self.ans = 1
        def dfs(node):
            for connected in graph[node]:
                if connected not in visited:
                    visited.add(connected)
                    self.ans += 1
                    dfs(connected)
                    
        dfs(0)
        return self.ans
