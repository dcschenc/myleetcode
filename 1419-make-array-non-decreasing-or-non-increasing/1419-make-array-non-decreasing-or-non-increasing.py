class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def solve(nums):
        # https://algo.monster/liteproblems/2263
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2263.Make%20Array%20Non-decreasing%20or%20Non-increasing
            n = len(nums)
            f = [[0] * 1001 for _ in range(n + 1)]
            for i, x in enumerate(nums, 1):
                mi = inf
                for j in range(1001):
                    if mi > f[i - 1][j]:
                        mi = f[i - 1][j]
                    f[i][j] = mi + abs(x - j)
            return min(f[n])

        return min(solve(nums), solve(nums[::-1]))