class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m, n = len(mat), len(mat[0])
        for _ in range(4):
            new_mat = [[0 for i in range(n)] for j in range(m)]
            # print(new_mat) 
            equal = True
            for i in range(m):
                for j in range(n):
                    new_mat[i][j] = mat[m-1-j][i]
                    if new_mat[i][j] != target[i][j]:
                        equal = False
            if equal:
                return True
            mat = new_mat
        return False
            