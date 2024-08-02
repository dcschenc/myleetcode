class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        s = [0] + list(accumulate(nums))
        return max(max(s[i + 1], s[-1] - s[i]) for i in range(len(nums)))
        
        n = len(nums)
        presum = [0] * n
        for i in range(len(nums)):
            presum[i] = nums[i]
            if i > 0:
                presum[i] += presum[i-1]
        ans = []
        for i in range(n):
            if i > 0:
                cur = max(presum[i], presum[-1] - presum[i-1])
            else:
                cur = max(presum[i], presum[-1])
            ans.append(cur)
        return max(ans)