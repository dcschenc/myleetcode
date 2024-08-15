class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2992.Number%20of%20Self-Divisible%20Permutations
        def dfs(idx):
            if idx == n:
                return 1
            total = 0
            for i in range(1, n+1):
                if used[i] == False and gcd(nums[i-1], idx + 1) == 1:
                    used[i] = True
                    total += dfs(idx + 1)
                    used[i] = False
            return total
        
        nums = [i for i in range(1, n+1)]
        used = [False] * (n + 1)
        return dfs(0)