class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        nums.sort()
        return 10 * (nums[0] + nums[1]) + (nums[2] + nums[3])

        num = str(num)
        num = sorted(num)
        return int(num[0] + num[2]) + int(num[1] + num[3])