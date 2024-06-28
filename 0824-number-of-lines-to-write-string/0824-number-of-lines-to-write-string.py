class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        res = [0, 0]
        curr = 0
        cnt = 1
        for c in s:
            idx = ord(c) - ord('a')
            if widths[idx] + curr > 100:
                curr = widths[idx]
                cnt += 1
            else:
                curr += widths[idx]
        res[0] = cnt
        res[1] = curr
        return res


