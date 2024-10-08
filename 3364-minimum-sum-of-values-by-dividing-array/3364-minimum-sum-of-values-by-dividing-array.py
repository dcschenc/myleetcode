class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3117.Minimum%20Sum%20of%20Values%20by%20Dividing%20Array
        @cache
        def dfs(i: int, j: int, a: int) -> int:
            if n - i < m - j:
                return inf
            if j == m:
                return 0 if i == n else inf
            a &= nums[i]
            if a < andValues[j]:
                return inf
            ans = dfs(i + 1, j, a)
            if a == andValues[j]:
                ans = min(ans, dfs(i + 1, j + 1, -1) + nums[i])
            return ans

        n, m = len(nums), len(andValues)
        ans = dfs(0, 0, -1)
        return ans if ans < inf else -1