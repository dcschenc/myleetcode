class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1099.Two%20Sum%20Less%20Than%20K
        nums.sort()
        ans = -1
        for i, x in enumerate(nums):
            j = bisect_left(nums, k - x, lo=i + 1) - 1
            if i < j:
                ans = max(ans, x + nums[j])
        return ans


        nums.sort()
        left, right = 0, len(nums) - 1
        max_sum = -1
        while left < right:
            cur = nums[left] + nums[right]
            if cur < k:
                max_sum = max(max_sum, cur)
                left += 1
            else:
                right -= 1
        return max_sum
