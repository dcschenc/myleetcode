class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3082.Find%20the%20Sum%20of%20the%20Power%20of%20All%20Subsequences
        mod = 10**9 + 7
        n = len(nums)
        f = [[0] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums, 1):
            for j in range(k + 1):
                f[i][j] = f[i - 1][j] * 2 % mod
                if j >= x:
                    f[i][j] = (f[i][j] + f[i - 1][j - x]) % mod
        return f[n][k]