class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        i, j, n = 0, len(s) - 1, len(s)
        while i < j:
            if s[i] != s[j]:
                if s[i] < s[j]:
                    s[j] = s[i]
                else:
                    s[i] = s[j]
            i += 1
            j -= 1
            
        return ''.join(s)