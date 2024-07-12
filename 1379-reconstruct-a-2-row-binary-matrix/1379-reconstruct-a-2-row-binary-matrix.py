class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1253.Reconstruct%20a%202-Row%20Binary%20Matrix
        n = len(colsum)
        ans = [[0] * n for _ in range(2)]
        for j, v in enumerate(colsum):
            if v == 2:
                ans[0][j] = ans[1][j] = 1
                upper, lower = upper - 1, lower - 1
            if v == 1:
                if upper > lower:
                    upper -= 1
                    ans[0][j] = 1
                else:
                    lower -= 1
                    ans[1][j] = 1
            if upper < 0 or lower < 0:
                return []
        return ans if lower == upper == 0 else []
        
        m, n = 2, len(colsum)
        ans = [[0 for j in range(n)] for i in range(2)]
        for j in range(n):
            if colsum[j] == 2:
                ans[0][j] = 1
                ans[1][j] = 1
                upper -= 1
                lower -= 1
                colsum[j] = 0
            
        if upper > 0:
            for j in range(n):
                if colsum[j] == 1 and ans[0][j] == 0:
                    ans[0][j] = 1
                    upper -= 1
                    colsum[j] = 0
                    if upper == 0:
                        break
        if lower > 0:
            for j in range(n):
                if colsum[j] == 1 and ans[1][j] == 0:
                    ans[1][j] = 1
                    colsum[j] = 0
                    lower -= 1
                    if lower == 0:
                        break
        if upper != 0 or lower != 0 or any(colsum):
            return []
        return ans
        