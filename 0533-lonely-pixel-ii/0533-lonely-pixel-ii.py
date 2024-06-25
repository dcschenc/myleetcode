class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        hm_rows = defaultdict(int)
        hm_cols = defaultdict(int)
        # same_rows = set()
        # for i in range(m):
        #     for j in range(i+1, m):
        #         if picture[i] == picture[j]:
        #             same_rows.add((i, j))
        #             same_rows.add((j, i))
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    hm_rows[i] += 1
                    hm_cols[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if hm_rows[i] == target == hm_cols[j]:
                    if all(picture[i] == picture[k] for k in range(m) if picture[k][j] == 'B'):
                    # if all((i, k) in same_rows for k in range(m) if picture[k][j] == 'B'):
                        ans += 1
        return ans