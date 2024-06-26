class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[[0 for _ in range(4)] for _ in range(n + 1)] for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if mat[i-1][j-1] == 1:
                    dp[i][j][0] = dp[i-1][j-1][0] + 1
                    dp[i][j][1] = dp[i-1][j][1] + 1
                    if j + 1 <= n:
                        dp[i][j][2] = dp[i-1][j+1][2] + 1
                    dp[i][j][3] = dp[i][j-1][3] + 1
                ans = max(ans, max(dp[i][j]))
        return ans                    
