from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    #### dijstra + dfs ####
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int: 
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1786.Number%20of%20Restricted%20Paths%20From%20First%20to%20Last%20Node
        @cache
        def dfs(u):
            if u == n:                
                return 1
            total_path = 0
            for v, _ in adj[u]:
                if shortest.get(v) < shortest.get(u):
                    total_path += dfs(v)
            return total_path
                  
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        shortest = {}
        minheap = [(0, n)]
        while minheap:
            dist, u = heappop(minheap)
            if u in shortest:
                continue
            shortest[u] = dist
            for v, w in adj[u]:
                if v not in shortest:
                    heappush(minheap, (dist + w, v))
        res = []
        path = []
        mod = 10**9 + 7
        return dfs(1)%mod

        

        