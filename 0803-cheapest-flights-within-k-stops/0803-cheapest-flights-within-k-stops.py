from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:    
        ##### Bellman-Ford #####    
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            new_dist = dist[:]
            for u, v, w in flights:
                if dist[u] != INF and dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist

        return dist[dst] if dist[dst] != INF else -1

        ####### dijstra #####
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
        minheap = [(0, src, -1)]
        visited = set()
        while minheap:
            price1, u, stops = heappop(minheap)            
            if u == dst:
                return price1       
            if (u, stops) in visited: 
                continue
            visited.add((u, stops))
            for v, price in adj[u]:
                if stops + 1 <= k:
                    heappush(minheap, (price1 + price, v, stops + 1))
        return -1
