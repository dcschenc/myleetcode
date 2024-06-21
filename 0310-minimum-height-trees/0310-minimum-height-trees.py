from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, so it's the root of the minimum height tree

        # Create an adjacency list
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        # Initialize leaves (nodes with only one neighbor)
        leaves = deque()
        for i in range(n):
            if indegree[i] == 1:
                leaves.append(i)

        remaining_nodes = n

        # Repeatedly remove leaves until only 1 or 2 nodes remain
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves

            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        leaves.append(neighbor)

        # The remaining nodes in 'leaves' are the potential roots of minimum height trees
        return list(leaves)
        
        if n <= 2:
            return [i for i in range(n)]
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                nb = adj[leaf].pop()
                adj[nb].remove(leaf)
                if len(adj[nb]) == 1:
                    new_leaves.append(nb)
            leaves = new_leaves
        return leaves

        
