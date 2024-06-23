class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:  
        ### without modify the grid
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                ans += 1
        return ans

        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    ans += 1
                    k = j + 1
                    while k <= n - 1 and board[i][k] == 'X':
                        board[i][k] = '.'
                        k += 1
                    if k == j + 1:
                        k = i + 1
                        while k <= m - 1 and board[k][j] == 'X':
                            board[k][j] = '.'
                            k += 1
        return ans