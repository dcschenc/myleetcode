class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        dp = {}
        dp[nums[0]] = 1
        for i in range(1, n):
            cur = math.sqrt(nums[i])
            dp[nums[i]] = 1
            if cur * cur == nums[i] and cur in dp:
                dp[nums[i]] = dp[cur] + 1
        mx = max(dp.values())
        return mx if mx > 1 else -1