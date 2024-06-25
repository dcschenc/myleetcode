class Solution:    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # ######### O(target_sum) #########
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        capacity = (total + target) // 2
        dp = [0] * (capacity + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for c in range(capacity, nums[i]-1, -1):
                dp[c] += dp[c-nums[i]]
        return dp[-1]

        s = sum(nums)
        if s < target or (s - target) % 2 != 0:
            return 0
        m, n = len(nums), (s - target) // 2
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]

        ########  O(n * target_sum) ######
        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0
        capacity = (total_sum + target) // 2
        n = len(nums)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(capacity + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]  
        return dp[n][capacity]

        ######## dfs, backtrack ########
        # # @cache
        # def dfs(summ:int, idx:int):
        #     key = (summ, idx)
        #     if key in hm:
        #         return hm[key]

        #     if idx == len(nums):
        #         if summ == target:
        #             return 1
        #         else:
        #             return 0

        #     num1 = dfs(summ-nums[idx], idx+1)
        #     num2 = dfs(summ+nums[idx], idx+1)

        #     hm[key] = num1+num2
        #     return num1 + num2
        
        # hm = {}
        # res = dfs(0, 0)
        # return res
        
        