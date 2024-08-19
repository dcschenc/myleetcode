class Solution:
    def numberOfWays(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3183.The%20Number%20of%20Ways%20to%20Make%20the%20Sum
        mod = 10**9 + 7
        coins = [1, 2, 6]
        f = [0] * (n + 1)
        f[0] = 1
        for x in coins:
            for j in range(x, n + 1):
                f[j] = (f[j] + f[j - x]) % mod
        ans = f[n]
        if n >= 4:
            ans = (ans + f[n - 4]) % mod
        if n >= 8:
            ans = (ans + f[n - 8]) % mod
        return ans
