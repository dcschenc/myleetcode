class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1039.Minimum%20Score%20Triangulation%20of%20Polygon
        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i + 1 == j:
        #         return 0
        #     return min(
        #         dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j]
        #         for k in range(i + 1, j)
        #     )

        # return dfs(0, len(values) - 1)

        n = len(values)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+2, n):
                m = float('inf')
                for k in range(i+1, j):
                    m = min(m, values[i] * values[j] * values[k] + dp[i][k] + dp[k][j])
                dp[i][j] = m
        return dp[0][n-1]