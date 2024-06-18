class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ### bit mat ###
        N = 9
        # Use binary number to check previous occurrence
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r] & (1 << pos):
                    return False
                rows[r] |= 1 << pos

                # Check the column
                if cols[c] & (1 << pos):
                    return False
                cols[c] |= 1 << pos

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx] & (1 << pos):
                    return False
                boxes[idx] |= 1 << pos

        return True

        m, n = len(board), len(board[0])
        rows, columns, squares = {}, {}, {}
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if i in rows:
                    rows[i].append(board[i][j])
                else:
                    rows[i] = [board[i][j]]
                    
                if j in columns:
                    columns[j].append(board[i][j])
                else:
                    columns[j] = [board[i][j]]
                
                key = i//3*3 + j//3
                # print(i,j, key)
                if key in squares:
                    squares[key].append(board[i][j])
                else:
                    squares[key] = [board[i][j]]
        # print(squares)
                    
        for i in rows:
            if len(set(rows[i])) != len(rows[i]):
                return False
        for i in columns:
            if len(set(columns[i])) != len(columns[i]):
                return False
        for i in squares:
            if len(set(squares[i])) != len(squares[i]):
                return False
        return True
        