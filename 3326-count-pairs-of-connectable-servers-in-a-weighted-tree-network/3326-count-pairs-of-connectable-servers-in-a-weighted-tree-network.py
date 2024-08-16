class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3067.Count%20Pairs%20of%20Connectable%20Servers%20in%20a%20Weighted%20Tree%20Network
        def dfs(a: int, fa: int, ws: int) -> int:
            cnt = 0 if ws % signalSpeed else 1
            for b, w in g[a]:
                if b != fa:
                    cnt += dfs(b, a, ws + w)
            return cnt

        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))
        ans = [0] * n
        for a in range(n):
            s = 0
            for b, w in g[a]:
                t = dfs(b, a, w)
                ans[a] += s * t
                s += t
        return ans