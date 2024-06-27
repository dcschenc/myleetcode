import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adj = {}
        # for i in range(1, n+1):
        #     adj[i] = []
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append([v, w])
        shortest = {}
        minheap = [(0, k)]
        while minheap:
            w1, u = heapq.heappop(minheap)
            if u in shortest:
                continue
            shortest[u] = w1
            for v, w2 in adj[u]:
                if v not in shortest:
                    heapq.heappush(minheap, (w1+w2, v))
      
        return max(shortest.values()) if len(shortest) == n else -1