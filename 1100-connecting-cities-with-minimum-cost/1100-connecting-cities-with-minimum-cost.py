from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        #### prim ####
        adj = defaultdict(list)
        for u, v, c in connections:
            adj[u].append((v, c))
            adj[v].append((u, c))
        minheap = []
        for v, c in adj[1]:
            heappush(minheap, (c, v))
        visited = set()
        visited.add(1)
        cost = 0
        while minheap:
            c, u = heappop(minheap)            
            if u in visited:
                continue
            cost += c
            visited.add(u)
            for v, c in adj[u]:
                if v not in visited:
                    heappush(minheap, (c, v))
        return cost if len(visited) == n else -1

        #### Kruskal ####
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        connections.sort(key=lambda x: x[2])
        p = list(range(n))
        ans = 0
        for x, y, cost in connections:
            x, y = x - 1, y - 1
            if find(x) == find(y):
                continue
            p[find(x)] = find(y)
            ans += cost
            n -= 1
            if n == 1:
                return ans
        return -1