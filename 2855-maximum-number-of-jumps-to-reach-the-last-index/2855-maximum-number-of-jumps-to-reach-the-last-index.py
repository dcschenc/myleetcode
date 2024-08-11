class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2770.Maximum%20Number%20of%20Jumps%20to%20Reach%20the%20Last%20Index
        @cache
        def dfs(i: int) -> int:
            if i == n - 1:
                return 0
            ans = -inf
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= target:
                    ans = max(ans, 1 + dfs(j))
            return ans

        n = len(nums)
        ans = dfs(0)
        return -1 if ans < 0 else ans
        
        n = len(nums)
        dp = [0] * (n)
        for i in range(1,  n):
            for j in range(i):
                if -target <= nums[i] - nums[j] <= target and (j == 0 or j > 0 and dp[j] > 0):
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n-1] if dp[n-1] != 0 else -1