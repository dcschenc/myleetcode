class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # @cache
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            ans = 0
            if i > j:
                ans = 0
            elif i == j: 
                ans = 1
            elif s[i] == s[j]:
                ans = dfs(i + 1, j - 1) + 2
            else:
                ans = max(dfs(i + 1, j), dfs(i, j - 1))
            cache[(i, j)] = ans
            return ans
            
        cache = {}
        return dfs(0, len(s) - 1)

        s1, s2 = s, s[::-1]
        n = len(s)
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # if i != 0 and j != 0:                    
                if s1[i-1] == s2[j-1]:
                    # if i != j:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max([dp[i-1][j], dp[i][j-1]])
        # print(dp)
        return dp[n][n]

