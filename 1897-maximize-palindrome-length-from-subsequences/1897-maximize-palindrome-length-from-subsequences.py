class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1771.Maximize%20Palindrome%20Length%20From%20Subsequences
        s = word1 + word2
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        ans = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < len(word1) <= j:
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return ans