class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff, mx = -1, nums[-1]
        for num in nums[::-1][1:]:
            if num < mx:
                diff = max(diff, mx - num)
            else:
                mx = num
        return diff
                