class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if word1 == word2:
        #     return 0
        # if word2 == '':
        #     return len(word1)
        # if word1 == '':
        #     return len(word2)
        m, n = len(word1), len(word2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        # for i in range(m+1):
        #     dp[i][0] = i
        # for j in range(n+1):
        #     dp[0][j] = j
        for i in range(0, m+1):
            for j in range(0, n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[m][n]
