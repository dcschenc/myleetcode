class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total, n = 0, 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                total += num
                n += 1
        return total // n if n != 0 else 0