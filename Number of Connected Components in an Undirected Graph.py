class Solution(object):
    def countComponents(self, n, edges):
        
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)
        
        seen = set()
        ans = 0
        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                ans+= 1
        
        return ans
