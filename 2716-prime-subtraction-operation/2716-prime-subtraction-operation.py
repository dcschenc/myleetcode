class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2601.Prime%20Subtraction%20Operation
        def get_primes(n):
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False
            for i in range(2, int(n**0.5) + 1):
                if primes[i]:
                    for j in range(i * i, n + 1, i):
                        primes[j] = False
            return [i for i in range(2, n) if primes[i]]
        
        primes = get_primes(1000)
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                continue
            j = bisect_right(primes, nums[i] - nums[i + 1])
            if j == len(primes) or primes[j] >= nums[i]:
                return False
            nums[i] -= primes[j]
        return True

        # for i, num in enumerate(nums):
        #     j = bisect_left(primes, x = num)   
        #     if i == 0:
        #         if j-1 >= 0:
        #             nums[i] -= primes[j-1]
        #     else:
        #         if nums[i] <= nums[i-1]:
        #             return False
        #         while nums[i] - primes[j-1] <= nums[i-1] and j-1 >=0:
        #             j -= 1
        #         if j - 1 >= 0:
        #             nums[i] -= primes[j-1]
        # return True
