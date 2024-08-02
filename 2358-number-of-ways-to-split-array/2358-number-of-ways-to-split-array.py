class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i-1] + nums[i-1]

        total = sum(nums)
        ans = 0
        for i in range(n-1):
            if presum[i+1] >= total - presum[i+1]:
                ans += 1
        return ans
