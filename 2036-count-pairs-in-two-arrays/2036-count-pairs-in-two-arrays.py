from collections import defaultdict
# Inspired from aaronyen:

# nums1[i] + nums1[j] > nums2[i] + nums2[j] is the equal to
# (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0

# So, if we define nums = [nums1[0]-nums2[0], nums1[1]-nums2[1], ...],
# This problem can be rewritten as:
# How many (i, j) pairs with i < j that nums[i] + nums[j] > 0

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1885.Count%20Pairs%20in%20Two%20Arrays
        n = len(nums1)
        d = [nums1[i] - nums2[i] for i in range(n)]
        d.sort()
        return sum(n - bisect_right(d, -v, lo=i + 1) for i, v in enumerate(d))


        # nums = [x - y for x, y in zip(nums1, nums2)]
        # nums.sort()
        
        # # print(nums)
        # n = len(nums)
        # res = 0
        # for i, x in enumerate(nums):
        #     if x > 0:
        #         res += n - i - 1
        #         continue

        #     l, r = i + 1, n - 1
        #     while l <= r:
        #         m = (l + r) >> 1
        #         if x + nums[m] > 0:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     res += n - l

        # return res