class Solution:
    def removeVowels(self, s: str) -> str:
        ans = ''
        for c in s:
            if c not in 'aeiou':
                ans += c
        return ans