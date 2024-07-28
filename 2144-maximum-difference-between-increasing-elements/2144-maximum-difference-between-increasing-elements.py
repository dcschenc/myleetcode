class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mi = inf
        ans = -1
        for x in nums:
            if x > mi:
                ans = max(ans, x - mi)
            else:
                mi = x
        return ans
        
        diff, mx = -1, nums[-1]
        for num in nums[::-1][1:]:
            if num < mx:
                diff = max(diff, mx - num)
            else:
                mx = num
        return diff
                