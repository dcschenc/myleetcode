class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2915.Length%20of%20the%20Longest%20Subsequence%20That%20Sums%20to%20Target
        n = len(nums)
        dp = [[-inf] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i, x in enumerate(nums, 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= x:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + 1)
                    
        return -1 if dp[n][target] <= 0 else dp[n][target]
