class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = nums[0]
        for num in nums:
            min_num = min(min_num, num)
        ans = 0
        while min_num > 0:
            ans += min_num % 10
            min_num = min_num // 10

        return 1 if ans % 2 == 0 else 0

        # if ans%2 == 0:
        #     return 1
        # else:
        #     return 0