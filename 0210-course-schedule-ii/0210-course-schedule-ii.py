from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the graph
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, precourse in prerequisites:
            graph[precourse].append(course)
            in_degree[course] += 1

        # Topological Sort using BFS
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        result_order = []
        while queue:
            course = queue.popleft()
            result_order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all courses can be finished (no cycles)
        if len(result_order) == numCourses:
            return result_order
        else:
            return []


        def dfs(src):
            if src in path:
                return False
            if src in visited:
                return True
            visited.add(src)
            path.add(src)
            for nb in adj[src]:
                res = dfs(nb)
                if res == False:
                    return False
            path.remove(src)
            topSort.append(src)
            return True
            
        
        adj = defaultdict(list)
        for course, precourse in prerequisites:
            adj[course].append(precourse)
        topSort = []
        path = set()
        visited = set()
        for i in range(numCourses):
            res = dfs(i)
            if not res:
                return []
        return topSort