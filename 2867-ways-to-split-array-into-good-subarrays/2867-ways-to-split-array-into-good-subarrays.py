class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2750.Ways%20to%20Split%20Array%20Into%20Good%20Subarrays
        mod = 10 ** 9 + 7
        ans, n, cur = 0, len(nums), 0
        for i in range(n):
            if nums[i] == 1:
                if ans == 0:
                    ans = 1
                else:
                    ans = ans * cur
                cur = 1
            else:
                cur += 1
        return ans % mod