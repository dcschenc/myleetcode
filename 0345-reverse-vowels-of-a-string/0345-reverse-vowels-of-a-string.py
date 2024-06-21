class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i < j:
            i_in = s[i] in vowels
            j_in = s[j] in vowels
            if i_in and j_in:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif i_in:
                j -= 1
            elif j_in:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s)