class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        
        for x, y, weight in flights:
            graph[x].append([y, weight])
            
        cost = [float("inf")] * n
        
        heap = [(0, src, 0)] #curr_distance, node, curr_stops
        
        while heap:
            curr_dist, node, curr_stops = heappop(heap)
            
            if curr_stops >= cost[node] or curr_stops > k+1:
                continue
            
            cost[node] = curr_stops
            
            if node == dst:
                return curr_dist
            
            for nei, price in graph[node]:
                heappush(heap, (curr_dist + price, nei, curr_stops + 1))

        
        return -1
