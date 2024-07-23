class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left, right = 0, 0
        n = len(s)
        for i in range(n):
            if i < n //2:
                if s[i] in 'aeiouAEIOU':
                    left += 1
            else:
                if s[i] in 'aeiouAEIOU':
                    right += 1
        return left == right