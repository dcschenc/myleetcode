class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2656.Maximum%20Sum%20With%20Exactly%20K%20Elements
        mx = max(nums)
        return mx * k + (k - 1) * k // 2
