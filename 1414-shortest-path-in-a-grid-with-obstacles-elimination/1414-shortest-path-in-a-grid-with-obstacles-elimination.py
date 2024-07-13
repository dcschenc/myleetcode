class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append((0, 0, 0))
        steps, visited = 0, set()
        while queue:
            for i in range(len(queue)):
                x, y, o = queue.popleft()
                if x == m-1 and y == n-1:
                    return steps
                if (x, y, o) in visited:
                    continue
                visited.add((x, y, o))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx <= m-1 and 0 <= ny <= n-1:
                        if grid[nx][ny] == 0:
                            queue.append((nx, ny, o))
                        else:
                            if o < k:
                                queue.append((nx, ny, o + 1))
            steps += 1
        return -1