class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = 0, 0
        for i in range(1, n, 2):
            d = 0
            if i - 1 >= 0:
                d = max(d, nums[i] - nums[i-1] + 1)
            if i + 1 < n:
                d = max(d, nums[i] - nums[i+1] + 1)
            a += d
        
        for i in range(0, n , 2):
            d = 0
            if i-1 >= 0:
                d = max(d, nums[i] - nums[i - 1] + 1)
            if i + 1 < n:
                d = max(d, nums[i] - nums[i + 1] + 1)
            b += d
        return min(a, b)