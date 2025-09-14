class Solution(object):
    def maximumDetonation(self, bombs):
        
        def dfs(node):
            count = 1
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    count += dfs(neighbour)
            return count
            
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if bombs[i][2]**2 >= (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2:
                    graph[i].append(j)
        
        ans = 0
        for i in range(len(bombs)):
            seen = {i}
            ans = max(ans, dfs(i))
        
        return ans 
