class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        cur = 0
        cnt = 1
        for c in s:
            idx = ord(c) - ord('a')
            if widths[idx] + cur > 100:
                cur = widths[idx]
                cnt += 1
            else:
                cur += widths[idx]
        return [cnt, cur]


