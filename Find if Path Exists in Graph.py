class Solution(object):
    def validPath(self, n, edges, source, destination):
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)
        
        seen = set()
        dfs(source)
        return destination in seen or source == destination
