from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue, visited, n = deque(), set(), len(arr)
        queue.append(start)
        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                if idx in visited:
                    continue
                if arr[idx] == 0:
                    return True
                visited.add(idx)
                if 0 <= idx + arr[idx] <= n - 1:
                    queue.append(idx + arr[idx])
                if 0 <= idx - arr[idx] <= n - 1:
                    queue.append(idx - arr[idx])
        return False
