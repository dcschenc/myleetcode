class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(row, col, num):
            # Check if the number is not in the current row, column, and subgrid
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = (row // 3) * 3, (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'  # Backtrack if the current choice does not lead to a solution
                        return False  # No valid choice found
            return True  # Entire board is filled
        
        
        solve()

        # """
        # Do not return anything, modify board in-place instead.
        # """
        # def backtrack(i, j):
        #     if i == n-1 and j == n-1 and board[i][j] != '.':
        #         return 'finish'         
            
        #     for v in range(1, 10):
        #         v = str(v)
        #         if is_valid(i, j, v):                    
        #             board[i][j] = v
        #             n_i, n_j = get_next_empty(i, j)
        #             if n_i > n-1:
        #                 return 'finish'
        #             res = backtrack(n_i, n_j)                    
        #             if res == 'finish':
        #                 return 'finish'
        #             board[i][j] = '.'
        
        # def get_next_empty(i, j):
        #     while i<n and board[i][j] != '.':
        #         j += 1
        #         if j > n-1:
        #             j = 0
        #             i+=1
        #     return (i, j)

        # def is_valid(i, j, v):            
        #     if v in board[i]:
        #         return False
        #     for ii in range(n):
        #         if board[ii][j] == v:
        #             return False
        #     row, col = 0, 0
        #     if 3<=i<6:
        #         row=3
        #     elif 6<=i<9:
        #         row = 6
        #     if 3<=j<6:
        #         col=3
        #     elif 6<=j<9:
        #         col = 6
        #     for k in range(row, row+3):
        #         for l in range(col, col+3):
        #             if v == board[k][l]:
        #                 return False
        #     return True

        # n = 9

        # for i in range(n):
        #     for j in range(n):
        #         if board[i][j] == '.':
        #             backtrack(i, j)
        #             break
        