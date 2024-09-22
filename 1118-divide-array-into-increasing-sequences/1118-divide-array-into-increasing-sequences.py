class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1121.Divide%20Array%20Into%20Increasing%20Sequences
        mx = max(len(list(x)) for _, x in groupby(nums))
        return mx * k <= len(nums)