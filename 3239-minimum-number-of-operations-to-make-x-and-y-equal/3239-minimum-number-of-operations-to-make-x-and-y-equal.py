class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque()
        queue.append(x)
        steps, visited = 0, set()
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == y:
                    return steps
                if cur in visited:
                    continue
                visited.add(cur)
                if cur % 11 == 0:
                    queue.append(cur // 11)
                if cur % 5 == 0:
                    queue.append(cur // 5)
                queue.append(cur - 1)
                queue.append(cur + 1)
            steps += 1
        return steps