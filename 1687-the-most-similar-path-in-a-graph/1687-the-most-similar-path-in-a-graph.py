class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1547.Minimum%20Cost%20to%20Cut%20a%20Stick
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)
        # Initialize the dp table with infinity
        dp = [[float('inf')] * m for _ in range(n)]
        # Initialize the previous node table to reconstruct the path
        prev = [[-1] * m for _ in range(n)]
        
        # Initialize the first column of dp table
        for i in range(n):
            dp[i][0] = int(names[i] != targetPath[0])
        
        # Fill the dp table
        for j in range(1, m):
            for i in range(n):
                for neighbor in graph[i]:
                    cost = dp[neighbor][j-1] + int(names[i] != targetPath[j])
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        prev[i][j] = neighbor
        
        # Find the minimum cost in the last column of dp table
        min_cost = float('inf')
        end_node = -1
        for i in range(n):
            if dp[i][m-1] < min_cost:
                min_cost = dp[i][m-1]
                end_node = i
        
        # Reconstruct the path
        path = [0] * m
        current_node = end_node
        for j in range(m-1, -1, -1):
            path[j] = current_node
            current_node = prev[current_node][j]
        
        return path


        g = [[] for _ in range(n)]
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)
        m = len(targetPath)
        f = [[inf] * n for _ in range(m)]
        pre = [[-1] * n for _ in range(m)]
        for j, s in enumerate(names):
            f[0][j] = targetPath[0] != s
        for i in range(1, m):
            for j in range(n):
                for k in g[j]:
                    if (t := f[i - 1][k] + (targetPath[i] != names[j])) < f[i][j]:
                        f[i][j] = t
                        pre[i][j] = k
        k = 0
        mi = inf
        for j in range(n):
            if f[-1][j] < mi:
                mi = f[-1][j]
                k = j
        ans = [0] * m
        for i in range(m - 1, -1, -1):
            ans[i] = k
            k = pre[i][k]
        return ans