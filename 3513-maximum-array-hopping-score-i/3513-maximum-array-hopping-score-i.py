class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3205.Maximum%20Array%20Hopping%20Score%20I
        @cache
        def dfs(i):
            if i >= n - 1:
                return 0
            ans = 0
            for j in range(i + 1, n):
                ans = max(ans, (j - i) * nums[j] + dfs(j))
            return ans

        n = len(nums)
        ans = dfs(0)
        return ans
