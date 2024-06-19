class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2: return 0
        # Sieve of Eratosthenes algorithm 
        primes = [True] * n
        for i in range(2, n):
            if primes[i]:
                for j in range(2*i, n, i):
                    primes[j] = False
                            
        return sum([1 if p else 0 for p in primes]) - 2

        # ans = []
        # for x in range(2, n // 2 + 1):
        #     y = n - x
        #     if primes[x] and primes[y]:
        #         ans.append([x, y])
        # return len(ans)
        # 
        # if n <= 2:
            # return 0

        # Create a boolean array "is_prime[0..n]" and initialize all entries it as True
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        # Use the Sieve of Eratosthenes algorithm to find primes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as not prime
                for j in range(i*i, n, i):
                    is_prime[j] = False

        # Count the number of primes
        count = sum(is_prime)
        return count
