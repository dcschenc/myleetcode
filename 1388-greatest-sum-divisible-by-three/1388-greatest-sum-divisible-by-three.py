class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1262.Greatest%20Sum%20Divisible%20by%20Three
        n = len(nums)
        dp = [[-float('inf') for j in range(3)] for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(3):
                mod = (nums[i-1] % 3 + j) % 3
                dp[i][j] = max(dp[i-1][j], dp[i-1][mod] + nums[i-1])
                
        return dp[n][0]

        # n = len(nums)
        # dp = [[-float('inf') for j in range(3)] for i in range(n+1)]
        # dp[0][0] = 0
        # for i in range(1, n+1):
        #     for j in range(3):
        #         dp[i][j]  = max(dp[i-1][j], dp[i-1][(nums[i-1]%3 + j)%3] + nums[i-1])
        # return dp[n][0]