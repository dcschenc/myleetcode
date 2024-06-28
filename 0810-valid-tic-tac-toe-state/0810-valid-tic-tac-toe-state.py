class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def count_symbol(symbol):
            count = 0
            for row in board:
                count += row.count(symbol)
            return count

        def check_winner(symbol):
            # Check rows
            for row in board:
                if all(cell == symbol for cell in row):
                    return True

            # Check columns
            for col in range(3):
                if all(board[row][col] == symbol for row in range(3)):
                    return True

            # Check diagonals
            if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
                return True

            return False

        count_X = count_symbol('X')
        count_O = count_symbol('O')

        if not (count_X == count_O or count_X == count_O + 1):
            return False

        if check_winner('X') and count_X != count_O + 1:
            return False

        if check_winner('O') and count_X != count_O:
            return False
        return True
            
        # m, n = len(board), len(board)
        # cnt_o, cnt_x = 0, 0        
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             cnt_o += 1
        #         elif board[i][j] == 'X':
        #             cnt_x += 1
        # if cnt_x < cnt_o or abs(cnt_x-cnt_o) > 1:
        #     return False
        # cnt_win = 0
        # x_win, o_win = False, False
        # for i in range(m):
        #     if board[i] == 'XXX':
        #         x_win = True
        #     if board[i] == 'OOO':
        #         o_win = True
        #         cnt_win += 1
        
        # for j in range(n):
        #     the_same = True
        #     for i in range(1, m):
        #         if board[i][j] != board[i-1][j]:
        #             the_same = False
        #     if the_same and board[0][j] != ' ':
        #         cnt_win += 1
        #         if board[0][j] == 'X':
        #             x_win = True
        #         if board[0][j] == 'O':
        #             o_win = True
        # if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        #     cnt_win += 1
        #     if board[0][0] == 'X':
        #         x_win = True
        #     if board[0][0] == 'O':
        #         o_win = True

        # if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        #     cnt_win += 1
        #     if board[0][2] == 'X':
        #         x_win = True
        #     if board[0][2] == 'O':
        #         o_win = True
        # # print(cnt_win)

        # if x_win and cnt_x == cnt_o:
        #     return False
        # if o_win and cnt_x > cnt_o:
        #     return False

        # if cnt_win > 1 and cnt_o + cnt_x != 9:
        #     return False
        
        # return True