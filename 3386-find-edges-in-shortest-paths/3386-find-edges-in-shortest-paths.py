class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        # https://leetcode.com/problems/find-edges-in-shortest-paths/solutions/5053007/python-simple-2-direction-dijkstra-s-algorithm/
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3123.Find%20Edges%20in%20Shortest%20Paths
        def findPath(source: int) -> List[int]:
            minHeap = [(0, source)]
            dist = [inf] * n
            dist[source] = 0
            while minHeap:
                x, u = heapq.heappop(minHeap)
                if dist[u] == x: # just an optimization so we don't need to handle the remaining longer path from the queue
                    for v, w in graph[u]:
                        if x + w < dist[v]:
                            dist[v] = x + w
                            heapq.heappush(minHeap, (x + w, v))
            return dist
        
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist0 = findPath(0)
        if dist0[-1] == inf:
            return [False] * len(edges)
        dist1 = findPath(n-1)        
        ans = []
        for u, v, w in edges:
            if dist0[u] + w + dist1[v] == dist0[-1] or dist1[u] + w + dist0[v] == dist1[0]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans