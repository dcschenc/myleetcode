class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0794.Valid%20Tic-Tac-Toe%20State
        def win(x):
            for i in range(3):
                if all(board[i][j] == x for j in range(3)):
                    return True
                if all(board[j][i] == x for j in range(3)):
                    return True
            if all(board[i][i] == x for i in range(3)):
                return True
            return all(board[i][2 - i] == x for i in range(3))

        x = sum(board[i][j] == 'X' for i in range(3) for j in range(3))
        o = sum(board[i][j] == 'O' for i in range(3) for j in range(3))
        if x != o and x - 1 != o:
            return False
        if win('X') and x - 1 != o:
            return False
        return not (win('O') and x != o)

        
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
            