class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur = 0
        min_sum = 0
        for num in nums:
            cur += num
            min_sum = min(min_sum, cur)
        
        if min_sum > 0:
            return 1
        else:
            return -min_sum + 1