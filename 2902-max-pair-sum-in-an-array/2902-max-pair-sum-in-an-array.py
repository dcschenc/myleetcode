class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        for a, b in combinations(nums, 2):
            if max(str(a)) == max(str(b)):
                ans = max(ans, a + b)
        return ans