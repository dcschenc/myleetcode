class TicTacToe:

    def __init__(self, n: int):
        self.board = [['-' for j in range(n)] for i in range(n)]     
        self.n = n   

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        self.board[row][col] = player
        if len(set(self.board[row])) == 1:
            return player
        if all(self.board[i][col] == player for i in range(n)):
            return player
        if row == col:
            i, j = 0, 0
            while i < n and j < n and self.board[i][j] == player:
                i += 1
                j += 1
            if i == n:
                return player
        if row + col == n - 1:
            i, j = 0, n - 1
            while i < n and j >= 0 and self.board[i][j] == player:
                i += 1
                j -= 1
            if i == n:
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)