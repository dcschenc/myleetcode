class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1818.Minimum%20Absolute%20Sum%20Difference
        # def binary_search(num):
        #     left, right = 0, len(arr) - 1
        #     while left < right:
        #         mid = (left + right) // 2
        #         if arr[mid] < num:                   
        #             left = mid + 1
        #         else:
        #             right = mid
        #     return left
            
        mod = 10**9 + 7
        nums = sorted(nums1)
        s = sum(abs(a - b) for a, b in zip(nums1, nums2)) % mod
        mx = 0
        for a, b in zip(nums1, nums2):
            d1, d2 = abs(a - b), inf
            i = bisect_left(nums, b)
            if i < len(nums):
                d2 = min(d2, abs(nums[i] - b))
            if i:
                d2 = min(d2, abs(nums[i - 1] - b))
            mx = max(mx, d1 - d2)
        return (s - mx + mod) % mod

        # mod = 10**9 + 7
        # nums = sorted(nums1)
        # s = sum(abs(a - b) for a, b in zip(nums1, nums2)) % mod
        # mx = 0
        # for a, b in zip(nums1, nums2):
        #     d1, d2 = abs(a - b), inf
        #     i = bisect_left(nums, b)
        #     if i < len(nums):
        #         d2 = min(d2, abs(nums[i] - b))
        #     if i:
        #         d2 = min(d2, abs(nums[i - 1] - b))
        #     mx = max(mx, d1 - d2)
        # return (s - mx + mod) % mod
