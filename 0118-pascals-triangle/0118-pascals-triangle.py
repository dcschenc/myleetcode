class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            level = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    level.append(1)
                else:
                    level.append(res[i-1][j-1] + res[i-1][j])
            res.append(level)
        return res

        res = [[]] * numRows
        for i in range(numRows):
            res[i] = [1] * (i+1)
            for j in range(1, i//2 + 1):
                res[i][i-j] =  res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res