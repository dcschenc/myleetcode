class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total, n = 0, len(nums)
        for i in range(n):
            cnt = 2
            sum_divisors = 1 + nums[i]
            for j in range(2, int(sqrt(nums[i])) + 1):
                if nums[i] % j == 0:
                    if j * j == nums[i]:
                        cnt += 1
                    else:
                        cnt += 2
                    sum_divisors += (j + nums[i] // j) 
            if cnt == 4:
                total += sum_divisors
        return total