class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = deque()
        queue.append(start)
        visited, steps = set(), 0    
        while queue:
            for _ in range(len(queue)):
                x = queue.popleft()
                if x == goal:
                    return steps
                if x in visited:
                    continue
                visited.add(x)                
                if x < 0 or x > 1000:
                    continue
                for num in nums:
                    queue.append(x + num)
                    queue.append(x - num)
                    queue.append(x ^ num)
            steps += 1
        return -1