class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0764.Largest%20Plus%20Sign
 
        mines = set([(x[0], x[1]) for x in mines])
        dp = [[[0 for k in range(4)] for j in range(n)] for i in range(n)]
        for i in range(n):            
            for j in range(n): 
                if (i, j) not in mines:               
                    if j > 0:                        
                        dp[i][j][0] = dp[i][j-1][0] + 1
                    else:
                        dp[i][j][0] = 1
                    if i > 0:
                        dp[i][j][1] = dp[i-1][j][1] + 1
                    else:
                        dp[i][j][1] = 1
            for j in range(n-1, -1, -1):
                if (i, j) not in mines:
                    if j == n-1:
                        dp[i][j][2] = 1
                    else:
                        dp[i][j][2] = dp[i][j + 1][2] + 1

        for i in range(n-1, -1, -1):
            for j in range(n):
                if (i, j) not in mines:
                    if i == n-1:
                        dp[i][j][3] = 1
                    else:
                        dp[i][j][3] = dp[i+1][j][3] + 1
        ans = 0
        for i in range(n):
            for j in range(n):    
                ans = max(ans, min(dp[i][j]))
        return ans            
                    