class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2919.Minimum%20Increment%20Operations%20to%20Make%20Array%20Beautiful
        f = g = h = 0
        for x in nums:
            f, g, h = g, h, min(f, g, h) + max(k - x, 0)
        return min(f, g, h)
