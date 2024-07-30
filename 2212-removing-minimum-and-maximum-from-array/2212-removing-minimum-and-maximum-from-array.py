class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2091.Removing%20Minimum%20and%20Maximum%20From%20Array
        mi = mx = 0
        for i, num in enumerate(nums):
            if num < nums[mi]:
                mi = i
            if num > nums[mx]:
                mx = i
        if mi > mx:
            mi, mx = mx, mi
        return min(mx + 1, len(nums) - mi, mi + 1 + len(nums) - mx)
                
        # n = len(nums)
        # min_idx, max_idx = 0, 0
        # min_val, max_val = float(inf), -float(inf)
        # for i in range(n):
        #     if nums[i] > max_val:
        #         max_val = nums[i]
        #         max_idx = i
        #     if nums[i] < min_val:
        #         min_val = nums[i]
        #         min_idx = i
        # mid = n // 2
        # if min_idx > max_idx:
        #     min_idx, max_idx = max_idx, min_idx

        # if min_idx <= mid and max_idx <= mid:
        #     return max_idx + 1
        # elif min_idx >= mid and max_idx >= mid:            
        #     return n - min_idx
        # elif min_idx <= mid and max_idx >= mid:
        #     return min(max_idx + 1, min_idx + 1 + (n - max_idx), n - min_idx)