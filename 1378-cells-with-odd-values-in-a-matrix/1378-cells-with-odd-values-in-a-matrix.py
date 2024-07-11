from collections import defaultdict
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        g = [[0] * n for _ in range(m)]
        for r, c in indices:
            for i in range(m):
                g[i][c] += 1
            for j in range(n):
                g[r][j] += 1
        return sum(v % 2 for row in g for v in row)

        # row = [0] * m
        # col = [0] * n
        # for r, c in indices:
        #     row[r] += 1
        #     col[c] += 1
        # return sum((i + j) % 2 for i in row for j in col)

        # row = [0] * m
        # col = [0] * n
        # for r, c in indices:
        #     row[r] += 1
        #     col[c] += 1
        # cnt1 = sum(v % 2 for v in row)
        # cnt2 = sum(v % 2 for v in col)
        # return cnt1 * (n - cnt2) + cnt2 * (m - cnt1)


        # ans = [[0 for i in range(n)] for _ in range(m)]
        # # r_cnt = defaultdict(int)
        # # c_cnt = defaultdict(int)
        # r_cnt = {r:0 for r in range(m)}
        # c_cnt = {c:0 for c in range(n)}
        # for r, c in indices:
        #     r_cnt[r] += 1
        #     c_cnt[c] += 1
        # odd_cols = len([col for col, c2 in c_cnt.items() if c2%2 == 1])      
        # even_cols = len([col for col, c2 in c_cnt.items() if c2%2 == 0])      
        # cnt = 0
        # for r, c1 in r_cnt.items():
        #     if c1 % 2 == 0:
        #         cnt += odd_cols           
        #     else:
        #         cnt += (n - odd_cols)
        # return cnt

