class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while i >=0:
            if s[i] == ' ':
                i-=1
            else:
                break
        # word = ''
        j = i
        while j>=0:
            if s[j] != ' ':
                # word += s[i]
                j-=1
            else:
                break
        # return len(word)
        return i - j
