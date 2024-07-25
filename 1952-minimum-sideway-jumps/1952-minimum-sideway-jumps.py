class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # https://leetcode.com/problems/minimum-sideway-jumps/
        def check(point, lane):
            if point == n - 1:
                return 0
            if obstacles[point + 1] != lane:
                return check(point + 1, lane)

            if point in memo:
                return memo[point]
            
            res = n
            for temp_l in range(1, 4):
                if temp_l != lane and obstacles[point] != temp_l:
                    res = min(res, 1 + check(point + 1, temp_l))
            memo[point] = res
            return res

        n = len(obstacles)
        memo = dict()        
        return check(0,2)

        n = len(obstacles)        
        dp = [[0, 0, 0, 0] for _ in range(n)]
        
        for i in range(n - 2, -1, -1):
            for cur_lane in range(4):
                if obstacles[i + 1] == cur_lane:
                    min_step = float(inf)
                    for lane in range(1, 4):                       
                        if obstacles[i + 1] != lane and obstacles[i] != lane:
                            min_step = min(min_step, dp[i + 1][lane] + 1)
                    dp[i][cur_lane] = min_step
                else:
                    dp[i][cur_lane] = dp[i + 1][cur_lane]
                    
        return dp[0][2]


        # dp = [1, 0, 1]
        # for i in range(1, len(obstacles)):
        #     if obstacles[i] == 1:
        #         dp[0] = float('inf')
        #     elif obstacles[i] == 2:
        #         dp[1] = float('inf')
        #     elif obstacles[i] == 3:
        #         dp[2] = float('inf')
        #     if obstacles[i - 1] == 1:
        #         dp[0] = min(dp[1], dp[2]) + 1
        #     elif obstacles[i - 1] == 2:
        #         dp[1] = min(dp[0], dp[2]) + 1
        #     elif obstacles[i - 1] == 3:
        #         dp[2] = min(dp[0], dp[1]) + 1
        # return min(dp)

        @cache
        def dfs(i, j, k):
            if j == n-1:
                return k
            ans = float(inf)
            if obstacles[j + 1] != i:
                ans = min(ans, dfs(i, j + 1, k))                             

            else:            
                if i == 1:
                    if obstacles[j] != 2:
                        dfs(2, j, k + 1)              
                    if obstacles[j] != 3:
                        dfs(3, j, k + 1)
                elif i == 2:
                    if obstacles[j] != 1:
                        dfs(1, j, k + 1)
                    if obstacles[j] != 3:
                        dfs(3, j, k + 1)
                else:               
                    if obstacles[j] != 1:
                        dfs(1, j, k + 1)
                    if obstacles[j] != 2:
                        dfs(2, j, k + 1)    
            return -1

        n, ans = len(obstacles), [float(inf)]
        dfs(2, 0, 0)
        return ans[0]                            