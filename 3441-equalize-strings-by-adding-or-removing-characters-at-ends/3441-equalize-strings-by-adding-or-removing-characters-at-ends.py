class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3135.Equalize%20Strings%20by%20Adding%20or%20Removing%20Characters%20at%20Ends
        m, n = len(initial), len(target)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        mx = 0
        for i, a in enumerate(initial, 1):
            for j, b in enumerate(target, 1):
                if a == b:
                    f[i][j] = f[i - 1][j - 1] + 1
                    mx = max(mx, f[i][j])
        return m + n - mx * 2
        