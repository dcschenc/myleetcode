class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1275.Find%20Winner%20on%20a%20Tic%20Tac%20Toe%20Game
        
        # n stands for the size of the board, n = 3 for the current game.
        n = 3
        # use rows and cols to record the value on each row and each column.
        # diag1 and diag2 to record value on diagonal or anti-diagonal.
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        # Two players having value of 1 and -1, player_1 with value = 1 places first.
        player = 1
        
        for row, col in moves:            
            rows[row] += player
            cols[col] += player
            
            # If this move is placed on diagonal or anti-diagonal, 
            if row == col:            
                diag += player
            if row + col == n - 1:
                anti_diag += player
                
            # check if this move meets any of the winning conditions.
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return "A" if player == 1 else "B"        
           
            player *= -1
            
        # If all moves are completed and there is still no result, we shall check if 
        # the grid is full or not. If so, the game ends with draw, otherwise pending.
        return "Draw" if len(moves) == n * n else "Pending" 

        # matrix = [[''] *3 for j in range(3)]
        # ch = 'X'
        # hm = {'X': 'A', 'O': 'B'}
        # for i, j in moves:
        #     matrix[i][j] = ch
        #     if ch == 'X':
        #         ch = 'O'
        #     else:
        #         ch = 'X'
        # for i in range(3):
        #     if len(set(matrix[i])) == 1:
        #       if matrix[i][0] in hm:
        #         return hm[matrix[i][0]] 
        #     columns = [matrix[row][i] for row in range(3)]
        #     if len(set(columns)) == 1:
        #       if matrix[0][i] in hm:
        #         return hm[matrix[0][i]] 
        # if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[0][0] != '':
        #     return hm[matrix[0][0]]
        # if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[0][2] != '':
        #     return hm[matrix[0][2]]
        # if len(moves) != 9:
        #     return 'Pending'
        # return 'Draw'
        