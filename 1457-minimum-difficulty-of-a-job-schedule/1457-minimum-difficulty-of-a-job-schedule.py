class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1335.Minimum%20Difficulty%20of%20a%20Job%20Schedule
        n = len(jobDifficulty)
        f = [[inf] * (d + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, d + 1):
                mx = 0
                for k in range(i, 0, -1):
                    mx = max(mx, jobDifficulty[k - 1])
                    f[i][j] = min(f[i][j], f[k - 1][j - 1] + mx)
        return -1 if f[n][d] >= inf else f[n][d]        