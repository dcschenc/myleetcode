class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2602.Minimum%20Operations%20to%20Make%20All%20Array%20Elements%20Equal
        ans, n = [], len(nums)
        nums.sort()
        # presum = [0] * (n + 1)
        # for i, num in enumerate(nums):
        #     presum[i + 1] = presum[i] + num
        presum = list(accumulate(nums, initial=0))
        for q in queries:
            idx = bisect_left(nums, q)
            left = idx * q - presum[idx]
            idx = bisect_right(nums, q)
            right = (presum[n] - presum[idx]) - (n - idx) * q
            ans.append(left + right)
        return ans