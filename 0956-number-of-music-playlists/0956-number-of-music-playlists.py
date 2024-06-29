class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0900-0999/0920.Number%20of%20Music%20Playlists
        dp = [[0 for j in range(n + 1)] for i in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                if j < k:
                    dp[i][j] = dp[i-1][j-1] * (n - (j -1))
                else:
                    dp[i][j] = dp[i-1][j-1] * (n - (j -1)) + dp[i-1][j] * (j - k)
        return dp[goal][n] % (10**9 + 7)