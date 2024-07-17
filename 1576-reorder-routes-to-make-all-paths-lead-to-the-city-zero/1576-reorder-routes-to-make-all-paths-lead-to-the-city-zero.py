class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:   
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1466.Reorder%20Routes%20to%20Make%20All%20Paths%20Lead%20to%20the%20City%20Zero
        def dfs(a: int, fa: int) -> int:
            return sum(c + dfs(b, a) for b, c in g[a] if b != fa)

        g = [[] for _ in range(n)]
        for a, b in connections:
            g[a].append((b, 1))
            g[b].append((a, 0))
        return dfs(0, -1)
        
        def dfs(node, parent):
            nonlocal count
            # if node in visited:
            #     return
            visited.add(node)
            for neighbor, direction in graph[node]:
                # if neighbor != parent:              
                if neighbor not in visited:      
                    count += direction  
                    dfs(neighbor, node)

        graph = {i: [] for i in range(n)}
        # If direction is 1, it's an outgoing edge; if 0, it's an incoming edge
        for u, v in connections:
            graph[u].append((v, 1))  
            graph[v].append((u, 0)) 
        count = 0
        visited = set()
        dfs(0, -1)  # Start DFS from city zero with a dummy parent
        return count        

        
