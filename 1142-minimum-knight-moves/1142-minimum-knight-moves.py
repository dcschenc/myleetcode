class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0, 0)])
        visited = set()
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if x == i and y == j:
                    return steps
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                    new_x, new_y = i + dx, j + dy
                    queue.append((new_x, new_y))
            steps += 1
