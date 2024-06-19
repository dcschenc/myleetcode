class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = ord('A') - 1
        res = 0
        for i, c in enumerate(columnTitle[::-1]):
          val = ord(c) - base
          res += val * pow(26, i)
        return res