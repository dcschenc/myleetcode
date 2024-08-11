class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2741.Special%20Permutations
        mod = 10**9 + 7
        n = len(nums)
        m = 1 << n
        f = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j, x in enumerate(nums):
                if i >> j & 1:
                    ii = i ^ (1 << j)
                    if ii == 0:
                        f[i][j] = 1
                        continue
                    for k, y in enumerate(nums):
                        if x % y == 0 or y % x == 0:
                            f[i][j] = (f[i][j] + f[ii][k]) % mod
        return sum(f[-1]) % mod
        
        def dfs(path):
            if len(path) == n:
                return 1
            total = 0
            for i in range(n):
                if seen[i] is False and (len(path) == 0 or path[-1] % nums[i] == 0 or nums[i] % path[-1] == 0):
                    seen[i] = True
                    total += dfs(path + [nums[i]])
                    seen[i] = False
            return total
        
        n = len(nums)
        seen = [False] * n
        return dfs([]) % (10 ** 9 + 7)

        