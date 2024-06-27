class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:        
        def is_target(m):
            if m[0][0] == 1 and m[0][1] == 2 and m[0][2] == 3 and m[1][0]==4 and m[1][1] == 5:
                return True
            return False

        queue = deque()
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    queue.append((board, i, j))
                    break        
        visited = set()
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cur, x, y = queue.popleft()
                if is_target(cur):
                    return steps
                t = tuple([tuple(row) for row in cur])
                if t in visited:
                    continue
                visited.add(t)
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 2 and 0 <= ny <= 2:
                        new_cur = copy.deepcopy(cur)
                        new_cur[x][y], new_cur[nx][ny] = new_cur[nx][ny], new_cur[x][y]
                        queue.append((new_cur, nx, ny))

            steps += 1
        return -1