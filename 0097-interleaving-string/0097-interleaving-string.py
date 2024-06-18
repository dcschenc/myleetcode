class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        i, j = 0, 0
        dp = [[False for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:                
                    # if j > 0:
                    if s3[j-1] == s2[j-1]:
                        dp[i][j] = dp[i][j-1]                        
                elif j == 0:
                    # if i > 0:
                    if s3[i-1] == s1[i-1]:
                        dp[i][j] = dp[i-1][j]           
                else:
                    if s3[i+j-1] == s1[i-1] and s3[i+j-1] != s2[j-1]: 
                        dp[i][j] = dp[i-1][j]
                    elif s3[i+j-1] == s2[j-1] and s3[i+j-1] != s1[i-1]:
                        dp[i][j] = dp[i][j-1]
                    elif s3[i+j-1] == s1[i-1] and s3[i+j-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j] or dp[i][j-1]
        # print(dp)
        return dp[m][n]