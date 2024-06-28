class Solution:
    def similarRGB(self, color: str) -> str:
        # letters = string.ascii_lowercase + string.digits
        letters = ['a', 'b', 'c', 'd', 'e', 'f'] + list(string.digits)
        mx = -float('inf')
        t1, t2, t3 = int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)
        for c1 in letters:
            b1 = int(c1 + c1, 16)
            for c2 in letters:
                b2 = int(c2 + c2, 16)
                for c3 in letters:
                    b3 = int(c3 + c3, 16)
                    cur = -(t1 - b1) ** 2 - (t2 - b2) ** 2 - (t3 - b3) ** 2
                    if cur > mx:
                        mx = cur
                        ans = '#' + c1 * 2 + c2 * 2 + c3 * 2
        return ans
