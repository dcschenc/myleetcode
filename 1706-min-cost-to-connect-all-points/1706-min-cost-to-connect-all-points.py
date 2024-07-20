from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ### prim ###
        adj = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i, n):                
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1])
                adj[i].append((j, dist))
                adj[j].append((i, dist))
                    
        visited = set()
        minheap = []
        for j, dist in adj[0]:
            heappush(minheap, (dist, j))
        visited.add(0)
        cost = 0
        while minheap:
            dist, i = heappop(minheap)
            if i in visited:
                continue
            visited.add(i)
            cost += dist
            for j, dist in adj[i]:
                if j not in visited:
                    heappush(minheap, (dist, j))
        return cost

        # adj = defaultdict(list)
        # for x1, y1 in points:
        #     for x2, y2 in points:
        #         if (x1 != x2 or y1 != y2):
        #             dist = abs(x1-x2) + abs(y1-y2)
        #             adj[(x1, y1)].append((x2, y2, dist))
        #             # adj[(x2, y2)].append((x1, y1, dist))
        # visited = set()
        # minheap = []
        # for x, y, dist in adj[(points[0][0], points[0][1])]:
        #     heappush(minheap, (dist, x, y))
        # visited.add((points[0][0], points[0][1]))
        # cost = 0
        # while minheap:
        #     dist, x, y = heappop(minheap)
        #     if (x, y) in visited:
        #         continue
        #     visited.add((x, y))
        #     cost += dist
        #     for x2, y2, dist in adj[(x, y)]:
        #         if (x2, y2) not in visited:
        #             heappush(minheap, (dist, x2, y2))
        # return cost