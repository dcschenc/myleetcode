class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def myPow(x, n):
            res = 1
            while n:
                if (n & 1) == 1:
                    res = res * x % mod
                x = x * x % mod
                n >>= 1
            return res

        return myPow(5, (n + 1) >> 1) * myPow(4, n >> 1) % mod
        
        primes = 4
        evens = 5
        total = 1
        mod = 10 ** 9 + 7
        # if n % 2 == 0:
        evens = 5 ** math.ceil(n / 2) % mod
        primes = 4 ** (n // 2) % mod
        return (evens * primes) % mod

        # for i in range(n) :
        #     if i % 2 == 0:
        #         total = total * 5
        #     else:
        #         total = total * 4
        #     total = total % mod
        # return total % mod