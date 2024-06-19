
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[True for j in range(n)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]

        dp = [float(inf) for i in range(n)]
        dp[0] = 0
        for i in range(1, n):
            for j in range(i + 1):
                if is_palindrome[j][i]:
                    if j == 0:
                        dp[i] = min(dp[i], 0)
                    else:
                        dp[i] = min(dp[i], dp[j-1] + 1)
        return dp[-1] 
        
