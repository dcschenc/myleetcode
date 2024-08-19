class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3179.Find%20the%20N-th%20Value%20After%20K%20Seconds
        a = [1] * n
        mod = 10**9 + 7
        for _ in range(k):
            for i in range(1, n):
                a[i] = (a[i] + a[i - 1]) % mod
        return a[n - 1]