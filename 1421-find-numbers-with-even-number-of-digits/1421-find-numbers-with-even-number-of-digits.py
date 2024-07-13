class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            num_digit = 1
            while num >= 10:
                num_digit += 1
                num = num / 10
            if num_digit % 2 == 0:
                count += 1
        return count