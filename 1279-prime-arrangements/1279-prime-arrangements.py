class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def count_prime(n):
            primes = [True] * (n + 1)
            cnt = 0
            for i in range(2, n+1):
                if primes[i]:
                    cnt += 1
                    for j in range(i + i, n + 1, i):
                        primes[j] = False
            return cnt
        
        prime_cnt = count_prime(n)
        return factorial(prime_cnt) * factorial(n - prime_cnt) % (10 ** 9 + 7)

        # def is_prime(m):
        #     for i in range(2, int(math.sqrt(m)) + 1):
        #         if m % i == 0:
        #             return False
        #     return True

        # primes = [2]
        # for i in range(3, n+1):
        #     if is_prime(i):
        #         primes.append(i)        
        # ans = 1
        # cnt = len(primes)
        # return (factorial(cnt) * factorial(n-cnt)) % (10**9 + 7)

