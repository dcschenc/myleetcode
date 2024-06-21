class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        presum = 0              
        seen = {0: -1}
        for i in range(n):
            presum += nums[i]
            key = presum - k
            if key in seen:
                ans = max(ans, i - seen[key])
            if presum not in seen:
                seen[presum] = i
        return ans