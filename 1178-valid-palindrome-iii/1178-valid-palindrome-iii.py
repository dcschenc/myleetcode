class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1216.Valid%20Palindrome%20III
        n = len(s)
        # Initialize the dp table
        dp = [[0] * n for _ in range(n)]

        # Single letters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill the dp table
        for length in range(2, n + 1):  # length of substring
            for i in range(n - length + 1):
                j = i + length - 1  # endpoint of the substring
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence
        lps_length = dp[0][n - 1]

        # Check if the longest palindromic subsequence is at least n - k
        return lps_length >= n - k

    
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                if dp[i][j] + k >= n:
                    return True
        return False
                