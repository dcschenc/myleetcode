class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate number of even and odd positions
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        # Use modular exponentiation
        def power_mod(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        
        # Calculate the result
        result = (power_mod(5, even_positions, MOD) * power_mod(4, odd_positions, MOD)) % MOD
        
        return result


        primes = 4
        evens = 5
        total = 1
        mod = 10 ** 9 + 7
        i = 1
        while i * 2 < math.ceil(n / 2) :
            evens = evens * evens % mod
            i = i * 2
        while i < math.ceil(n/2):
            evens = evens * 5 % mod
            i += 1

        i = 1
        while i *2 < n // 2:
            primes = primes * primes % mod
            i = i * 2       
        while i < n // 2:
            primes = primes * 4 % mod
            i += 1

        return evens * primes % mod

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