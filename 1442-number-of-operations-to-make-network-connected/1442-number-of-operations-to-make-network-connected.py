from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    dfs(child)

        if len(connections) < n-1:
            return -1

        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count - 1