class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2718.Sum%20of%20Matrix%20After%20Queries
        row = set()
        col = set()
        ans = 0
        for t, i, v in queries[::-1]:
            if t == 0:
                if i not in row:
                    ans += v * (n - len(col))
                    row.add(i)
            else:
                if i not in col:
                    ans += v * (n - len(row))
                    col.add(i)
        return ans

        # rows, cols = defaultdict(tuple), defaultdict(tuple)
        
        # for i, (t, idx, val) in enumerate(queries):
        #     if t == 0:
        #         rows[idx] = (val, i)
        #     else:
        #         cols[idx] = (val, i)

        # total = 0
        # for i in range(n):
        #     for j in range(n):
        #         cur = 0
        #         time_r = -1
        #         if i in rows:
        #             val_r, time_r = rows[i]
        #             cur = val_r
        #         if j in cols:
        #             val_c, time_c = cols[j]
        #             if time_c > time_r:
        #                 cur = val_c
        #         total += cur
        # return total
        