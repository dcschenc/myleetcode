class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        return sum(
            grid[i][j] and (row[i] > 1 or col[j] > 1)
            for i in range(m)
            for j in range(n)
        )
        # m, n = len(grid), len(grid[0])
        # rows = defaultdict(list)
        # cols = defaultdict(list)
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             rows[i].append((i, j))
        #             cols[j].append((i, j))
        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             queue = deque([(i, j)])
        #             visited = set()
        #             cur = 0
        #             while queue:
        #                 for _ in range(len(queue)):
        #                     x, y = queue.popleft()
        #                     grid[x][y] = 0
        #                     if (x, y) in visited:
        #                         continue
        #                     cur += 1
        #                     visited.add((x, y))                            
        #                     for new_x, new_y in rows[x]:
        #                         if grid[new_x][new_y] == 1:
        #                             queue.append((new_x, new_y))
        #                     for new_x, new_y in cols[y]:
        #                         if grid[new_x][new_y] == 1:
        #                             queue.append((new_x, new_y))
        #             if cur > 1:
        #                 ans += cur
        # return ans
        