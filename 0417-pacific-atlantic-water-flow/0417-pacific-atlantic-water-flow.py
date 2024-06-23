class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue, ocean):
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()                
                    ocean.add((x, y))
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and heights[new_x][new_y] >= heights[x][y]:
                            if (new_x, new_y) in ocean:
                                continue
                            queue.append((new_x, new_y))

        m, n = len(heights), len(heights[0])
        pocean, aocean = set(), set()
        for j in range(n):
            pocean.add((0, j))
            aocean.add((m-1, j))
        for i in range(m):
            pocean.add((i, 0))
            aocean.add((i, n-1))
        queue = deque(pocean)
        bfs(queue, pocean)

        queue = deque(aocean)
        bfs(queue, aocean)

        ans = pocean & aocean
        return list(ans)