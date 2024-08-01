class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_c, end_c = s[0], s[3]
        start_r, end_r = int(s[1]), int(s[4])
        c = start_c
        result = []
        while c <= end_c:
            for i in range(start_r, end_r + 1):
                result.append(c + str(i))
            c = chr(ord(c) + 1)
        return result