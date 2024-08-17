class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_pos = {}
        for i, c in enumerate(word):
            if c.islower():
                char_pos[c] = i
                continue
            if c not in char_pos:                
                char_pos[c] = i
        ans = 0
        for c in string.ascii_lowercase:
            if c in char_pos and c.upper() in char_pos and char_pos[c] < char_pos[c.upper()]:
                ans += 1
        return ans
                
