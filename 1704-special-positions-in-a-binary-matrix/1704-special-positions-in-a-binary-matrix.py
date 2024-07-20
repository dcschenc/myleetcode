class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        return sum(mat[i][j] for j in range(n) for i in range(m) if rows[i] == 1 and cols[j] == 1 and mat[i][j] == 1)