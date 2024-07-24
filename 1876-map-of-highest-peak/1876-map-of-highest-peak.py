class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1765.Map%20of%20Highest%20Peak
        queue = deque()
        m, n = len(isWater), len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    # isWater[i][j] = 0
        visited = set()
        # levels = 1
        while queue:
            for _ in range(len(queue)):
                x, y, h = queue.popleft()
                if (x, y) in visited:
                    continue
                isWater[x][y] = h
                visited.add((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x <= m-1 and 0 <= new_y <= n-1:
                        queue.append((new_x, new_y, h + 1))
            # levels += 1

        return isWater
        