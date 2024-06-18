class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, down, left, right = 0, n - 1, 0, n - 1
        count = 0
        res = [[0] * n for _ in range(n)]
        while count < n * n:
            for j in range(left, right + 1):
                count += 1
                res[top][j] = count

            for i in range(top + 1, down + 1):
                count += 1
                res[i][right] = count

            if top <= down:
                for j in range(right - 1, left - 1, -1):
                    count += 1
                    res[down][j] = count
                
            if left <= right:
                for i in range(down - 1, top, -1):
                    count += 1
                    res[i][left] = count

            top += 1
            down -= 1
            left += 1
            right -= 1
        # print(res)
        return res

