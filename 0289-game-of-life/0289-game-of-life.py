import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        def count_live_neighbors(x, y):
            live_neighbors = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (board[nx][ny] == 1 or board[nx][ny] == -1):
                    live_neighbors += 1

            return live_neighbors

        for i in range(rows):
            for j in range(cols):
                live_neighbors = count_live_neighbors(i, j)

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        # Rule 1 and Rule 3
                        board[i][j] = -1  # Mark as dead (was alive)
                else:
                    if live_neighbors == 3:
                        # Rule 4
                        board[i][j] = 2  # Mark as alive (was dead)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    # Convert marked alive cells to 1
                    board[i][j] = 1
                elif board[i][j] == -1:
                    # Convert marked dead cells to 0
                    board[i][j] = 0

        # m, n = len(board), len(board[0])
        # board_c = copy.deepcopy(board)
        # for i in range(m):
        #     for j in range(n):
        #         nbs = [(i-1, j), (i-1,j-1), (i-1, j+1), (i,j-1), (i,j+1), (i+1, j), (i+1, j-1), (i+1, j+1)]
        #         ones, zeros = 0, 0
        #         for x, y in nbs:
        #             if 0 <= x <= m-1 and 0 <= y <= n-1:
        #                 if board_c[x][y] == 1:
        #                     ones += 1
        #                 else:
        #                     zeros += 1
        #         # print(i, j, ones, zeros)
        #         if board[i][j] == 1:
        #             if ones < 2 or ones >3:
        #                 board[i][j] = 0                   
        #         elif board[i][j] == 0 and ones == 3:
        #             board[i][j] = 1
