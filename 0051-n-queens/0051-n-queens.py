class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                res.append([''.join(tmp) for tmp in chestboard])                
                return
            for col in range(n):
                if is_valid(row, col):
                    chestboard[row][col] = 'Q'
                    backtrack(row + 1)
                    chestboard[row][col] = '.'
        
        def is_valid(row, col):
            for i in range(row):
                if chestboard[i][col] == 'Q':
                    return False
            i, j = row - 1, col - 1
            #### 45 direction ####
            while i >= 0 and j >= 0:
                if chestboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            ### 135 direction ####
            while i  >= 0 and j < n:
                if chestboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True        

        res = []
        chestboard = [['.'] * n for i in range(n)]
        backtrack(0)
        return res