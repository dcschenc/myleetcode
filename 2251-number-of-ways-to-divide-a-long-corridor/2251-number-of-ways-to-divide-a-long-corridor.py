class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2147.Number%20of%20Ways%20to%20Divide%20a%20Long%20Corridor
        @cache
        def dfs(i, cnt):
            if i == n:
                return int(cnt == 2)
            if corridor[i] == 'S':
                cnt += 1
            if cnt > 2:
                return 0
            ans = dfs(i + 1, cnt)
            if cnt == 2:
                ans += dfs(i + 1, 0)
                ans %= mod
            return ans

        n = len(corridor)
        mod = 10**9 + 7
        ans = dfs(0, 0)
        dfs.cache_clear()
        return ans        