from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1091.Shortest%20Path%20in%20Binary%20Matrix
        m, n = len(grid), len(grid[0])
        queue = deque()
        if grid[0][0] != 0:
            return -1
        queue.append((0, 0, 1))
        visited = set()
        dr = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        while queue:
            for i in range(len(queue)):
                x, y, length = queue.popleft()
                if x == m-1 and y == n-1:
                    return length
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                for dx, dy in dr:
                    newX, newY = dx + x, dy + y
                    if 0 <= newX <= m-1 and 0<= newY <= n-1 and grid[newX][newY] == 0:
                        queue.append((newX, newY, length + 1))
        return -1

        # if grid[0][0]:
        #     return -1
        # n = len(grid)
        # grid[0][0] = 1
        # q = deque([(0, 0)])
        # ans = 1
        # while q:
        #     for _ in range(len(q)):
        #         i, j = q.popleft()
        #         if i == j == n - 1:
        #             return ans
        #         for x in range(i - 1, i + 2):
        #             for y in range(j - 1, j + 2):
        #                 if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
        #                     grid[x][y] = 1
        #                     q.append((x, y))
        #     ans += 1
        # return -1
