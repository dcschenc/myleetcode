class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1958.Check%20if%20Move%20is%20Legal
        m, n = len(board), len(board[0])
        dr = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
        for dx, dy in dr:
            cnt = 0
            x, y = rMove, cMove
            while 0 <= x + dx <= m-1 and 0 <= y + dy <= n-1:
                x, y = x + dx, y + dy
                cur = board[x][y]
                if cur not in ['.', color]:
                    cnt += 1
                elif cur == '.':
                    break
                elif cur == color:
                    if cnt > 0:
                        return True
                    else:
                        break
        return False

        # i = rMove - 1
        # cnt = 0
        # while i > 0:
        #     cur = board[i][cMove]
        #     if cur not in ['.', color]:
        #         cnt += 1
        #     elif cur == '.' :
        #         break
        #     elif cur == color:
        #         if cnt > 0:
        #             return True
        #     i -= 1