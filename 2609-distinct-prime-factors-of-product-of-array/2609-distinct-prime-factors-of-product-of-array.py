class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2521.Distinct%20Prime%20Factors%20of%20Product%20of%20Array
        def find_prime_factors(n):
            factors = set()
            divisor = 2
            while divisor <= n:
                if n % divisor == 0:
                    factors.add(divisor)
                    n = n / divisor
                else:
                    divisor += 1
            return factors

        ans = set()
        for num in nums:
            ans = ans | find_prime_factors(num)
        return len(ans)
