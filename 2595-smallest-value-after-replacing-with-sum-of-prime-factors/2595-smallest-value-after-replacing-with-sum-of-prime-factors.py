class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factors_sum(num):
            factors_sum = 0
            i = 2
            while i * i <= num:
                if num % i == 0:
                    factors_sum += i
                    num //= i
                else:
                    i += 1
            if num > 1:
                factors_sum += num
            return factors_sum

        while True:
            prime_sum = prime_factors_sum(n)
            if prime_sum == n:
                return n
            n = prime_sum