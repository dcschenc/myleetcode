class Solution:
    def waysToReachStair(self, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3154.Find%20Number%20of%20Ways%20to%20Reach%20the%20K-th%20Stair
        @cache
        def dfs(i: int, j: int, jump: int) -> int:
            if i > k + 1:
                return 0
            ans = int(i == k)
            if i > 0 and j == 0:
                ans += dfs(i - 1, 1, jump)
            ans += dfs(i + (1 << jump), 0, jump + 1)
            return ans

        return dfs(1, 0, 0)