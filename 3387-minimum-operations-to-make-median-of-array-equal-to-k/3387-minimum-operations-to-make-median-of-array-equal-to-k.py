class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3107.Minimum%20Operations%20to%20Make%20Median%20of%20Array%20Equal%20to%20K
        nums.sort()
        n = len(nums)
        m = n >> 1
        ans = abs(nums[m] - k)
        if nums[m] > k:
            for i in range(m - 1, -1, -1):
                if nums[i] <= k:
                    break
                ans += nums[i] - k
        else:
            for i in range(m + 1, n):
                if nums[i] >= k:
                    break
                ans += k - nums[i]
        return ans