class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2453.Destroy%20Sequential%20Targets
        cnt = Counter(v % space for v in nums)
        ans = mx = 0
        for v in nums:
            t = cnt[v % space]
            if t > mx or (t == mx and v < ans):
                ans = v
                mx = t
        return ans