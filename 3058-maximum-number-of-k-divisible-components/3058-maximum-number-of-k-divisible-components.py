class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2872.Maximum%20Number%20of%20K-Divisible%20Components
        def dfs(i: int, fa: int) -> int:
            s = values[i]
            for j in g[i]:
                if j != fa:
                    s += dfs(j, i)
            nonlocal ans
            ans += s % k == 0
            return s

        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = 0
        dfs(0, -1)
        return ans