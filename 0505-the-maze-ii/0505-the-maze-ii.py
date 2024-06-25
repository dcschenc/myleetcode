class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n, d = len(maze), len(maze[0]), defaultdict(int)
        for i in range(m):
            for j in range(n):
                d[(i, j)] = float("inf")

        d[tuple(start)] = 0

        minheap = [(start[0], start[1], 0)]

        while minheap:
            x, y, dist = heapq.heappop(minheap)

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny, weight = x, y, 0

                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] != 1:
                    nx += dx
                    ny += dy
                    weight += 1

                if d[(nx, ny)] > dist + weight:
                    d[(nx, ny)] = dist + weight
                    heapq.heappush(minheap, (nx, ny, d[(nx, ny)]))

        return d[tuple(destination)] if d[tuple(destination)] != float("inf") else -1

