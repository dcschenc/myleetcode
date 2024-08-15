class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if i % 2 == 1:
                    if mat[i][(j + k) % n] != mat[i][j]:
                        return False
                else:
                    if mat[i][(j + n - k) % n] != mat[i][j]:
                        return False
        return True
            