class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1332.Remove%20Palindromic%20Subsequences
        return 1 if s == s[::-1] else 2
        
        if len(s) == 0:
            return 0
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return 2
            left += 1
            right -= 1
        return 1