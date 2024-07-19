class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1547.Minimum%20Cost%20to%20Cut%20a%20Stick
        cuts.extend([0, n])
        cuts.sort()
        m = len(cuts)
        f = [[0] * m for _ in range(m)]
        for l in range(2, m):
            for i in range(m - l):
                j = i + l
                f[i][j] = inf
                for k in range(i + 1, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + cuts[j] - cuts[i])
        return f[0][-1]
        