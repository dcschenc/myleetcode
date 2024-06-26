from collections import defaultdict
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for a, b in ops:
            m = min(m, a)
            n = min(n, b)
        return m * n

        # if len(ops) == 0:
        #     return m*n
        # min_x, min_y = m+1, n+1
        # for x, y in ops:
        #     if x < min_x:
        #         min_x = x
        #     if y < min_y:
        #         min_y = y        
            
        # return min_x * min_y

        # mat = [[0 for j in range(n)] for i in range(m)]
        # if len(ops) == 0:
        #     return m*n
        # hm = defaultdict(int)
        # for x, y in ops:
        #     for i in range(x):
        #         for j in range(y):
        #             hm[(i,j)] +=1
        # max_num = 0
        
        # for k, v in hm.items():
        #     if v >= max_num:
        #         max_num = v
        # cnt = 0
        # for k, v in hm.items():
        #     if v == max_num:
        #         cnt += 1
        # return cnt

        # max_num = 0
        # for i in range(m):
        #     for j in range(n):
        #         if max_num < mat[i][j]:
        #             max_num = mat[i][j]
        # cnt = 0
        # for i in range(m):
        #     for j in range(n):
        #         if max_num == mat[i][j]:
        #             cnt +=1
        # return cnt