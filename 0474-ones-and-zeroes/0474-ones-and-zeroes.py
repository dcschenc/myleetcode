class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ####### TC: O(l * m * n) ###########
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            ones = s.count('1')
            zeros = len(s) - ones
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)

        return dp[m][n]

        # dp = [[0] * (n+1) for _ in range(m+1)]
        # for s in strs:
        #     zeros, ones = 0, 0
        #     for c in s:
        #         if c == '0':
        #             zeros += 1
        #         else:
        #             ones += 1
        #     for i in range(m, zeros-1, -1):
        #         for j in range(n, ones-1, -1):
        #             dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        # return dp[m][n]

