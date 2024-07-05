from collections import deque
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        i, j = 0, 0
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'R':
                    i, j = x, y
                    break               
                    
        dr = [(1, 0), (0, 1), (-1, 0), (0,-1)]      
        count = 0
        for dx, dy in dr: 
            x, y = i, j
            while 0 <= x + dx <= m-1 and 0 <= y + dy <= n-1:
                x, y = x + dx, y + dy
                if board[x][y] == "p":
                    count += 1
                    break
                if board[x][y] == "B":
                    break
        return count