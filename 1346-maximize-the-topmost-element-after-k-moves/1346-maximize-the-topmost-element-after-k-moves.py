class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            if k % 2 == 1:
                return -1
            else:
                return nums[0]

        mx = max(nums[:k-1], default = -1)
        if k < n:
            mx = max(mx, nums[k])
        return mx