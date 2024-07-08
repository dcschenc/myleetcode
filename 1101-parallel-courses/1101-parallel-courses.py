from collections import deque, defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        degree = [0] * (n + 1)
        for u, v in relations:
            adj[u].append(v)
            degree[v] += 1

        queue = deque()
        for i in range(1, n+1):
            if degree[i] == 0:
                queue.append(i)        
        count = 0
        course_taken = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                course_taken += 1
                for nb in adj[node]:
                    degree[nb] -= 1
                    if degree[nb] == 0:
                        queue.append(nb)
            count += 1
        return count if course_taken == n else -1
        