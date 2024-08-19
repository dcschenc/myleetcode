class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3201.Find%20the%20Maximum%20Length%20of%20Valid%20Subsequence%20I
        k = 2
        f = [[0] * k for _ in range(k)]
        ans = 0
        for x in nums:
            x %= k
            for j in range(k):
                y = (j - x + k) % k
                f[x][y] = f[y][x] + 1
                ans = max(ans, f[x][y])
        return ans
