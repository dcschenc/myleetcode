class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(i, j):
            if vis[i][j]:
                return
            vis[i][j] = True
            if [i, j] == destination:
                return
            for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                x, y = i, j
                while 0 <= x + a < m and 0 <= y + b < n and maze[x + a][y + b] == 0:
                    x, y = x + a, y + b
                dfs(x, y)

        m, n = len(maze), len(maze[0])
        vis = [[False] * n for _ in range(m)]
        dfs(start[0], start[1])
        return vis[destination[0]][destination[1]]

        m = len(maze)
        n = len(maze[0])
        visit = [[False] * n for _ in range(m)]
        queue = deque()
        
        queue.append(start)
        visit[start[0]][start[1]] = True
        dirX = [0, 1, 0, -1]
        dirY = [-1, 0, 1, 0]

        while queue:
            curr = queue.popleft()
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True

            for i in range(4):
                r = curr[0]
                c = curr[1]
                # Move the ball in the chosen direction until it can.
                while r >= 0 and r < m and c >= 0 and c < n and maze[r][c] == 0:
                    r += dirX[i]
                    c += dirY[i]
                # Revert the last move to get the cell to which the ball rolls.
                r -= dirX[i]
                c -= dirY[i]
                if not visit[r][c]:
                    queue.append([r, c])
                    visit[r][c] = True
        return False
        

        # def dfs(x, y, direction):                        
        #     if x == destination[0] and y == destination[1]:
        #         if direction == 'U' and (x + 1 > m-1 or maze[x+1][y] == 1):
        #             return True          
        #         if direction == 'D' and (x - 1 < 0 or maze[x-1][y] == 1):
        #             return True
        #         if direction == 'L' and (y + 1 > n - 1 or maze[x][y+1] == 1):
        #             return True
        #         if direction == 'R' and (y - 1 < 0 or maze[x][y-1] == 1):
        #             return True
        #         return False

        #     if (x, y) in visited:
        #         return False
            

        #     ans = False
        #     if x-1 >= 0 and maze[x - 1][y] == 0:
        #         ans |= dfs(x-1, y, 'D')
        #     if x+1 <=m-1 and maze[x + 1][y] == 0:
        #         ans |= dfs(x+1, y, 'U')
        #     if y+1 <= n-1  and maze[x][y+1]== 0:
        #         ans |= dfs(x, y+1, 'L')
        #     if y-1 >=0 and maze[x][y-1] == 0:
        #         ans |= dfs(x, y-1, 'R')
        #     visited.add((x, y))
        #     return ans

        # m, n = len(maze), len(maze[0])
        # x, y = destination[0], destination[1]
        # visited = set()
        # return dfs(start[0], start[1], '')
