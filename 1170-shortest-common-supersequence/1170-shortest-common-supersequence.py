class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1092.Shortest%20Common%20Supersequence
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the table using bottom-up dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The length of the shortest common supersequence
        length = m + n - dp[m][n]

        # Reconstruct the shortest common supersequence
        result = [''] * length
        i, j, k = m, n, length - 1

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result[k] = str1[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result[k] = str1[i - 1]
                i -= 1
            else:
                result[k] = str2[j - 1]
                j -= 1
            k -= 1

        while i > 0:
            result[k] = str1[i - 1]
            i -= 1
            k -= 1

        while j > 0:
            result[k] = str2[j - 1]
            j -= 1
            k -= 1

        return ''.join(result)