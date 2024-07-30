from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2101.Detonate%20the%20Maximum%20Bombs
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]
                if ri**2 >= (xi-xj) **2 + (yi-yj)**2:
                    graph[i].append(j)        
        result = 0
        for i in range(n):            
            visited = set()
            queue = deque()
            queue.append(i)
            count = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    count += 1
                    for nb in graph[node]:
                        queue.append(nb)
            result = max(result, count)
        return result



