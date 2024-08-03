from itertools import accumulate
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2302.Count%20Subarrays%20With%20Score%20Less%20Than%20K
        s = list(accumulate(nums, initial=0))
        ans = 0
        for i in range(1, len(s)):
            left, right = 0, i
            while left < right:
                mid = (left + right + 1) >> 1
                if (s[i] - s[i - mid]) * mid < k:
                    left = mid
                else:
                    right = mid - 1
            ans += left
        return ans
        