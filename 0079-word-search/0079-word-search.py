class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0000-0099/0079.Word%20Search
        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word) - 1:
                return board[i][j] == word[k]
            if board[i][j] != word[k]:
                return False
            c = board[i][j]
            board[i][j] = "0"
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                ok = 0 <= x < m and 0 <= y < n and board[x][y] != "0"
                if ok and dfs(x, y, k + 1):
                    return True
            board[i][j] = c
            return False

        m, n = len(board), len(board[0])
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))


        ############## chaohai's solution ############
        def backtrack(word, i, j):
            if len(word) == 0:
                return True
            if len(word) == 1 and word[0] == board[i][j]:
                return True

            if word[0] == board[i][j]:
                tmp = board[i][j]
                board[i][j] = '.'
                moves = [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]                
                for new_i, new_j in moves:
                    if 0<= new_i<m and 0 <= new_j<n and board[new_i][new_j] != '.':                        
                        res = backtrack(word[1:], new_i, new_j)
                        if res:
                            return res
                board[i][j] = tmp
            return False
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                res = backtrack(word, i, j)
                if res:
                    return True
        return False