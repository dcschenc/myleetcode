class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int: 
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1473.Paint%20House%20III
        f = [[[inf] * (target + 1) for _ in range(n + 1)] for _ in range(m)]
        if houses[0] == 0:
            for j, c in enumerate(cost[0], 1):
                f[0][j][1] = c
        else:
            f[0][houses[0]][1] = 0
        for i in range(1, m):
            if houses[i] == 0:
                for j in range(1, n + 1):
                    for k in range(1, min(target + 1, i + 2)):
                        for j0 in range(1, n + 1):
                            if j == j0:
                                f[i][j][k] = min(
                                    f[i][j][k], f[i - 1][j][k] + cost[i][j - 1]
                                )
                            else:
                                f[i][j][k] = min(
                                    f[i][j][k], f[i - 1][j0][k - 1] + cost[i][j - 1]
                                )
            else:
                j = houses[i]
                for k in range(1, min(target + 1, i + 2)):
                    for j0 in range(1, n + 1):
                        if j == j0:
                            f[i][j][k] = min(f[i][j][k], f[i - 1][j][k])
                        else:
                            f[i][j][k] = min(f[i][j][k], f[i - 1][j0][k - 1])

        ans = min(f[-1][j][target] for j in range(1, n + 1))
        return -1 if ans >= inf else ans
        
        dp = [[[float('inf') for k in range(n)] for j in range(target + 1)] for i in range(m)]               
        if houses[0] == 0:
            for k in range(n):            
                dp[0][1][k] = cost[0][k]
        else:
            dp[0][1][houses[0]-1] = 0            

        for i in range(1, m):
            for j in range(1, target + 1):                
                if houses[i] != 0:
                    color = houses[i] - 1
                    for k in range(n):
                        if k == color:
                            dp[i][j][color] = min(dp[i][j][color], dp[i-1][j][k])
                        else:
                            dp[i][j][color] = min(dp[i][j][color], dp[i-1][j-1][k])
                else:
                    for k in range(n):
                        for k2 in range(n):
                            if k == k2:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k2] + cost[i][k])
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][k2] + cost[i][k])
        # print(dp)
        return  min(dp[m-1][target]) if min(dp[m-1][target]) != float(inf) else -1