class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2971.Find%20Polygon%20With%20the%20Largest%20Perimeter
        nums.sort()
        s = list(accumulate(nums, initial=0))
        ans = -1
        for k in range(3, len(nums) + 1):
            if s[k - 1] > nums[k - 1]:
                ans = max(ans, s[k])
        return ans

        # nums.sort()
        # i, n = 2, len(nums)
        # l, cur = 0, sum(nums[:2])
        # mx = -1
        # while i < n:
        #     if cur > nums[i]:
        #         mx = max(mx, cur + nums[i])
        #     # else:
        #     #     l += 1
        #     cur += nums[i]
        #     i += 1
        # return mx