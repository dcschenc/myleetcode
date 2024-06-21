class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        num_of_primes = len(primes)
        dp = [0] * n
        dp[0] = 1
        pointers = [0] * num_of_primes
        
        for i in range(1, n):
            next_num = min(dp[pointers[j]] * primes[j] for j in range(num_of_primes))
            dp[i] = next_num
            for j in range(num_of_primes):
                if next_num == dp[pointers[j]] * primes[j]:
                    pointers[j] += 1
        
        return dp[-1]        