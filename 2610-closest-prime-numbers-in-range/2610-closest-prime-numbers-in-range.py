class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2523.Closest%20Prime%20Numbers%20in%20Range
        def sieve(n):
            prime = [True] * (n + 1)
            for i in range(2, n // 2):
                if prime[i]:
                    for jj in range(2 * i, n + 1, i):
                        prime[jj] = False
            return [i for i in range(2, n + 1) if prime[i]]
        
        primes = sieve(right)
        inRange = False
        minDiff = float("inf")
        ans = [-1, -1]
        n = len(primes)
        for i in range(0, n - 1):
            if not inRange:
                if primes[i] >= left:
                    inRange = True                    
            if inRange:
                l = primes[i]
                r = primes[i + 1]
                if (r - l) < minDiff:
                    minDiff = r - l
                    ans = [l, r]
        return ans