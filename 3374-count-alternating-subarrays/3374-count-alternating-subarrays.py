class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3101.Count%20Alternating%20Subarrays
        ans = s = 1
        for a, b in pairwise(nums):
            s = s + 1 if a != b else 1
            ans += s
        return ans


        n = len(nums)
        i = left = ans = 0
        while i < n:
            if i > 0 and nums[i] == nums[i-1]:
                left = i
            ans += (i - left + 1)
            i += 1
        return ans
        