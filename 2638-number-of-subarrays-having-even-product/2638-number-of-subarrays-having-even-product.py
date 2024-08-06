class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/number-of-subarrays-having-even-product/solutions/4351091/python-solution-one-pass-track-last-seen-even-index/
        ans = 0
        last_even = -1
        for i, n in enumerate(nums):
            if n % 2 == 0:
                ans += (i + 1)
                last_even = i
            elif last_even != -1:
                ans += (last_even + 1)
        
        return ans


