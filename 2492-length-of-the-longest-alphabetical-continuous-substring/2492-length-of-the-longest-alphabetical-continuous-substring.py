class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2414.Length%20of%20the%20Longest%20Alphabetical%20Continuous%20Substring
        l, r = 0, 1
        ans = 1
        while r < len(s):
            if ord(s[r]) != ord(s[r-1]) + 1:
                ans = max(ans, r - l)
                l = r   
            elif r == len(s) - 1:
                ans = max(ans, r - l + 1)     
            r += 1
        return ans
        