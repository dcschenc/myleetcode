class Solution:
    def makePalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        cnt = 0
        while left < right:
            if s[left] != s[right] and left != right:
                cnt += 1
            left += 1
            right -= 1
        return cnt <= 2
