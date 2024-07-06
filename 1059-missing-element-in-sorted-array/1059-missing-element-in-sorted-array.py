class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1060.Missing%20Element%20in%20Sorted%20Array/README.md
        def missing(i: int) -> int:
            return nums[i] - nums[0] - i

        n = len(nums)
        if k > missing(n - 1):
            return nums[n - 1] + k - missing(n - 1)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if missing(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return nums[l - 1] + k - missing(l - 1)

        # i, n = 1, len(nums)
        # cnt = 0
        # while i < n:
        #     if nums[i-1] + (k - cnt) < nums[i]:
        #         return nums[i-1] + k - cnt
        #     cnt += nums[i] - nums[i-1] - 1
        #     i += 1 
        # return nums[n-1] + (k - cnt)
        