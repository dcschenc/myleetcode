class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].isalpha() is False:
                i += 1
                continue
            if s[j].isalpha() is False:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)