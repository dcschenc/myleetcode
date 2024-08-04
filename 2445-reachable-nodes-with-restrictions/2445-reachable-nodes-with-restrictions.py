class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2368.Reachable%20Nodes%20With%20Restrictions
        def dfs(i: int) -> int:
            vis.add(i)
            return 1 + sum(j not in vis and dfs(j) for j in g[i])

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vis = set(restricted)
        return dfs(0)
        
                
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        restricted = set(restricted)
        queue, visited = deque(), set()
        queue.append(0)
        ans = 0
        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                if idx in visited:
                    continue
                visited.add(idx)
                for nb in graph[idx]:
                    if nb not in restricted and nb not in visited:
                        queue.append(nb)
        return len(visited)
