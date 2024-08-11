class Solution:
    def finalString(self, s: str) -> str:
        ans = ''
        for c in s:
            if c != 'i':
                ans += c
            else:
                ans = ans[::-1]
        return ans