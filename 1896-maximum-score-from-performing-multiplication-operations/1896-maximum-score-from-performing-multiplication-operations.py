class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1770.Maximum%20Score%20from%20Performing%20Multiplication%20Operations
        @cache
        def dp(i, j, k):
            if k >= m or i >= n or j < 0:
                return 0
            a = dp(i + 1, j, k + 1) + nums[i] * multipliers[k]
            b = dp(i, j - 1, k + 1) + nums[j] * multipliers[k]
            return max(a, b)

        n = len(nums)
        m = len(multipliers)
        return dp(0, n - 1, 0)


        n, m = len(nums), len(multipliers)
        dp = [[float('-inf')] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        for step in range(1, m + 1):
            for left in range(step + 1):
                right = step - left
                mult = multipliers[step - 1]
                if left > 0:
                    dp[step][left] = max(dp[step][left], mult * nums[left - 1]  + dp[step - 1][left - 1])

                if right > 0:
                    dp[step][left] = max(dp[step][left], mult * nums[n - right] + dp[step - 1][left])

        return max(dp[m])


        # n, m = len(nums), len(multipliers)
        # dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        # for i in range(m - 1, -1, -1):
        #     for left in range(i, -1, -1):
        #         mult = multipliers[i]
        #         right = n - 1 - (i - left)
        #         dp[i][left] = max(mult * nums[left]  + dp[i + 1][left + 1], 
        #                           mult * nums[right] + dp[i + 1][left])        
        # return dp[0][0]
        
        # # lru_cache from functools automatically memoizes the function
        # @lru_cache(2000)
        # def dp(i, left):
        #     # Base case
        #     if i == m: 
        #         return 0

        #     mult = multipliers[i]
        #     right = n - 1 - (i - left)
            
        #     # Recurrence relation
        #     return max(mult * nums[left] + dp(i + 1, left + 1), mult * nums[right] + dp(i + 1, left))
                       
        # n, m = len(nums), len(multipliers)
        # return dp(0, 0)