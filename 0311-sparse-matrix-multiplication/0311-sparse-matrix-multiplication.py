class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        k, n = len(mat2), len(mat2[0])
        ans = [[0 for j in range(n)] for i in range(m)]
        row_hm, col_hm = defaultdict(list), defaultdict(list)
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    row_hm[i].append(j)
        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0:
                    col_hm[j].append(i)

        for i in range(m):
            for j in range(n):
                for idx1 in row_hm[i]:
                    for idx2 in col_hm[j]:
                        if idx1 == idx2:
                            ans[i][j] += mat1[i][idx1] * mat2[idx2][j]
        return ans