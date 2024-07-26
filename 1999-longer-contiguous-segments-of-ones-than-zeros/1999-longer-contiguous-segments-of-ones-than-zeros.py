class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1869.Longer%20Contiguous%20Segments%20of%20Ones%20than%20Zeros
        len0, len1, n = 0, 0, len(s)
        i = 0
        while i < n:
            if s[i] == '0':
                j = i + 1
                while j < n and s[j] == '0':
                    j += 1
                len0 = max(len0, j - i)
                i = j
            else:
                j = i + 1
                while j < n and s[j] == '1':
                    j += 1
                len1 = max(len1, j - i)
                i = j
        return len1 > len0
        