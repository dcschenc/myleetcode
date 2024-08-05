class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2436.Minimum%20Split%20Into%20Subarrays%20With%20GCD%20Greater%20Than%20One
        ans, g = 1, 0
        for x in nums:
            g = gcd(g, x)
            if g == 1:
                ans += 1
                g = x
        return ans