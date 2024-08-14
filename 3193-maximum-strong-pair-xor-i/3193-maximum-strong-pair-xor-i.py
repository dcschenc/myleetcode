class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        for x, y in combinations(nums, 2):
            if abs(x - y) <= min(x, y):
                ans = max(ans, x ^ y)
        return ans