from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, precourse in prerequisites:
            adj[precourse].append(course)
            in_degree[course] += 1
        
        # Topological Sort using BFS
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all courses can be finished (no cycles)
        return all(in_degree[i] == 0 for i in range(numCourses))


        def dfs(src):
            if src in path:
                return False
            if src in visited:
                return 
            visited.add(src)
            path.add(src)
            for nb in adj[src]:
                res = dfs(nb)
                if res is False:
                    return False
            path.remove(src)
            return 

        adj = defaultdict(list)
        for i, j in prerequisites:
            adj[i].append(j)
        path = set()
        visited = set()
        for i in range(numCourses):
            res = dfs(i)
            if res is False:
                return False
        return True