class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt_u, cnt_r = 0, 0
        for c in moves:
            if c == 'U':
                cnt_u += 1
            elif c == 'D':
                cnt_u -=1
            elif c == 'R':
                cnt_r += 1
            else:
                cnt_r -= 1
        return cnt_u == 0 and cnt_r == 0