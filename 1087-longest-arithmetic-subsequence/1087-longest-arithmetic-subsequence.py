
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                key = nums[i] - nums[j]
                dp[i][key] = dp[j][key] + 1
                ans = max(ans, dp[i][key] + 1)
        return ans
        
