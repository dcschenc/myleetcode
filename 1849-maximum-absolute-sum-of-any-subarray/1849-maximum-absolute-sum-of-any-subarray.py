class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1749.Maximum%20Absolute%20Sum%20of%20Any%20Subarray
        f = g = 0
        ans = 0
        for x in nums:
            f = max(f, 0) + x
            g = min(g, 0) + x
            ans = max(ans, f, abs(g))
        return ans
                
        n = len(nums)
        po, ng = 0, 0
        ans = 0
        for i in range(n):            
            po += nums[i]
            ng += nums[i]
            ans = max(ans, po, abs(ng))
            if po < 0:
                po = 0
            if ng > 0:
                ng = 0
        return ans