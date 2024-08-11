class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]: 
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2761.Prime%20Pairs%20With%20Target%20Sum          
        def get_primes(n):
            is_prime = [True] * n
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i*i, n, i):
                        is_prime[j] = False
            return [i for i in range(1, n) if is_prime[i]]
            # primes = []
            # for i in range(1, n):
            #     if is_prime[i]:
            #         primes.append(i)
            # return primes

        primes = get_primes(n + 1)
        # print(primes)
        seen = set()
        ans = []
        for i in range(len(primes)):
            if n - primes[i] in seen:
                ans.append([n - primes[i], primes[i]])
            if primes[i] * 2 == n:
                ans.append([primes[i], primes[i]])
            seen.add(primes[i])
        ans.sort(key=lambda x: x[0])
        return ans
            