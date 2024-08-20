class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3243.Shortest%20Distance%20After%20Road%20Addition%20Queries%20I
        def bfs(i: int) -> int:
            q = deque([i])
            vis = [False] * n
            vis[i] = True
            d = 0
            while 1:
                for _ in range(len(q)):
                    u = q.popleft()
                    if u == n - 1:
                        return d
                    for v in g[u]:
                        if not vis[v]:
                            vis[v] = True
                            q.append(v)
                d += 1

        g = [[i + 1] for i in range(n - 1)]
        ans = []
        for u, v in queries:
            g[u].append(v)
            ans.append(bfs(0))
        return ans    