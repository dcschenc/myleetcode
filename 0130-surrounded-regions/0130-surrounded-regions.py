from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if (i in [0, m-1] or j in [0, n-1]) and board[i][j] == 'O':
                    board[i][j] = 'M'
                    queue.append((i,j))
        while queue:
            i, j = queue.popleft()
            moves = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for x, y in moves:
                if 0 <= x <= m-1 and 0 <= y <= n-1 and board[x][y] == 'O':
                    board[x][y] = 'M'
                    queue.append((x, y))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'M':
                    board[i][j] = 'O'
        