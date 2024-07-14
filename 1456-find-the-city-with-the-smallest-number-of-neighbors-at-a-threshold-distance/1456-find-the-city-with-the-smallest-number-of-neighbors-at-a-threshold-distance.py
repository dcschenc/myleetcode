from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # distances = [[float('inf')] * n for _ in range(n)]
        # for u, v, w in edges:
        #     distances[u][v] = w
        #     distances[v][u] = w

        # for i in range(n):
        #     distances[i][i] = 0

        # # Floyd-Warshall 
        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        # result_city = -1
        # min_neighbors = float('inf')

        # # Iterate through each city and count neighbors within the threshold
        # for i in range(n):
        #     count_neighbors = sum(1 for j in range(n) if distances[i][j] <= distanceThreshold)

        #     if count_neighbors <= min_neighbors:
        #         min_neighbors = count_neighbors
        #         result_city = i

        # return result_city

        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1334.Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        result = []
        for i in range(n):
            shortest = {}
            minheap = [(0, i)]     
            while minheap:
                dist, node = heappop(minheap)
                if node in shortest:
                    continue
                shortest[node] = dist
                for nb, w in adj[node]:
                    if dist + w <= distanceThreshold:
                        heappush(minheap, (dist + w, nb))
            result.append(len([x for x in shortest if x != i]))
        
        min_cities = min(result) 
        number = -1
        # print(result, min_cities)
        for i in range(len(result)):
            if min_cities == result[i]:
                number = i
        return number
