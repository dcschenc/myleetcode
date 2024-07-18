from heapq import heappop, heappush
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))
        
        min_heap = [(-1, start_node)]
        visited = set()
        while min_heap:
            prob, node = heappop(min_heap)
            prob = -prob
            if node == end_node:
                return prob
            visited.add(node)
            for nb, succ_prob in adj[node]:
                if nb not in visited:
                    heappush(min_heap, (-prob*succ_prob, nb))
        return 0.0