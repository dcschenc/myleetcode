class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            t, m = divmod(num, 3)
            total += min(3 - m, m)
        return total