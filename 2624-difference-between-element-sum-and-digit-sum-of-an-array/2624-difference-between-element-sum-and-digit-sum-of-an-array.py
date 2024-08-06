class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            for c in str(num):
                total += int(c)
        return abs(total - sum(nums))