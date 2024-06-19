class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        left, right = 0, 0
        while right < len(s):
            while right != len(s) and s[right] != ' ':
                right += 1
            i, j = left, right - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            left, right = right + 1, right + 1
        return s