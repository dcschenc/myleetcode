class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = total = 0
        n = len(nums)
        min_len = float('inf')
        for right in range(n):
            total += nums[right]
            while total >= target and left <= right:                
                min_len = min(right-left+1, min_len)
                total -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len
                