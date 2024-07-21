class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1605.Find%20Valid%20Matrix%20Given%20Row%20and%20Column%20Sums
        m, n = len(rowSum), len(colSum)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x = min(rowSum[i], colSum[j])
                ans[i][j] = x
                rowSum[i] -= x
                colSum[j] -= x
        return ans