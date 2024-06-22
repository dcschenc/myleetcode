class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # m, n = len(s), len(t)
        # if m == 0:
        #     return True
        # elif n == 0:
        #     return False
        # if s[0] == t[0]:
        #     return self.isSubsequence(s[1:], t[1:])
        # else:
        #     return self.isSubsequence(s, t[1:])
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j <n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == m:
            return True
        return False

        # t_dic = {}
        # for c in dic
        # m, n = len(s), len(t)
        # dp = [[False for i in range(n+1)] for j in range(m+1)]
        # print(dp)
        # dp[0][0] = True
        
        # for i in range(1,m):
        #     for j in range(1,n):
        #         print(s[i-1], t[j-1], dp[i-1][j-1])
        #         if s[i-1] == t[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #             break
        #         else:
        #             # print(i,j)
        #             dp[i][j] = dp[i-1][j-2]
        # return dp[m][n]