class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3122.Minimum%20Number%20of%20Operations%20to%20Satisfy%20Conditions
        m, n = len(grid), len(grid[0])
        f = [[inf] * 10 for _ in range(n)]
        for i in range(n):
            cnt = [0] * 10
            for j in range(m):
                cnt[grid[j][i]] += 1
            if i == 0:
                for j in range(10):
                    f[i][j] = m - cnt[j]
            else:
                for j in range(10):
                    for k in range(10):
                        if k != j:
                            f[i][j] = min(f[i][j], f[i - 1][k] + m - cnt[j])
        return min(f[-1])        