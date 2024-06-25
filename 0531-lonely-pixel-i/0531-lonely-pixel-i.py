from collections import defaultdict
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        hm_rows = defaultdict(int)
        hm_cols = defaultdict(int)
        m, n = len(picture), len(picture[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    hm_rows[i] += 1
                    hm_cols[j] += 1
                    
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if hm_rows[i] == 1 and hm_cols[j] == 1:
                        cnt += 1
        return cnt