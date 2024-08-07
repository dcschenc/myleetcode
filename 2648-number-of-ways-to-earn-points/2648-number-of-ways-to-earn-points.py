class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        @cache
        def dfs(i, cur):
            if cur == target:
                return 1
            if i >= n:
                return 0
            ans = 0
            cnt, score = types[i]
            for j in range(cnt + 1):
                if cur + j * score <= target:
                    ans += dfs(i + 1, cur + j * score)
                else:
                    break
            return ans % mod
        
        n = len(types)
        mod = 10 ** 9 + 7
        ans = dfs(0, 0)        
        return ans % mod

        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2585.Number%20of%20Ways%20to%20Earn%20Points
        n = len(types)
        mod = 10**9 + 7
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            count, marks = types[i - 1]
            for j in range(target + 1):
                for k in range(count + 1):
                    if j >= k * marks:
                        f[i][j] = (f[i][j] + f[i - 1][j - k * marks]) % mod
        return f[n][target]
