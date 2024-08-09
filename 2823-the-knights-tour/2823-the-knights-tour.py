class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2664.The%20Knight%E2%80%99s%20Tour
        def backtrack(x, y, cur):
            if cur == m * n:
                return True
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    if dx in [-1, 1] and dy in [-2, 2] or dx in [-2, 2] and dy in [-1, 1]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and board[new_x][new_y] == -1:
                            board[new_x][new_y] = cur
                            if backtrack(new_x, new_y, cur + 1):
                                return True
                            board[new_x][new_y] = -1
            return False
        board = [[-1 for j in range(n)] for i in range(m)]
        board[r][c] = 0   
        backtrack(r, c, 1)
        return board