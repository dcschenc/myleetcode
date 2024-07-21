from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(list)
        for x, y in roads:
            adj[x].append(y)
            adj[y].append(x)

        max_conn = 0
        for i in range(n):
            for j in range(i+1, n):
                num = len(adj[i]) + len(adj[j])
                if i in adj[j]:
                    num -= 1
                max_conn = max(max_conn, num)
        return max_conn
