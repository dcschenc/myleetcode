from collections import deque
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:               
        queue = deque()
        queue.append((rCenter, cCenter))
        result = []
        visited = set()
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                result.append([x, y])
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= x + dx <= rows-1 and 0 <= y + dy <= cols-1:                        
                        queue.append((x+dx, y+dy))
        return result
