from collections import deque, defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:        
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1462.Course%20Schedule%20IV
        n = numCourses
        f = [[False] * n for _ in range(n)]
        for a, b in prerequisites:
            f[a][b] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if f[i][k] and f[k][j]:
                        f[i][j] = True
        return [f[a][b] for a, b in queries]

        # store the graph
        adj = {node: set() for node in range(numCourses)}    
        # store indegree info for each node
        indegree = defaultdict(int)     
        # store the prerequisites info for each node
        pre_nodes = defaultdict(set)   
        
        # create the graph
        for pre, post in prerequisites:
            adj[pre].add(post)
            indegree[post] += 1
        
        # add 0 degree nodes into queue for topological sort
        queue = deque([])
        for n in adj:
            if indegree[n] == 0:
                queue.append(n)
        
        # use BFS to do topological sort to create a prerequisite lookup dictionary
        while queue:
            cur = queue.popleft()
            for nb in adj[cur]:
                pre_nodes[nb].add(cur)  
                 # add all the preqs for current node to the neighbor node's preqs
                pre_nodes[nb].update(pre_nodes[cur])   
                # regular topological search operations
                indegree[nb] -= 1         
                if indegree[nb] == 0:
                    queue.append(nb)
        
        # traverse the queries and return the results
        result = [True if u in pre_nodes[v] else False for u, v in queries]
        
        return result

        def bfs(src, dst):
            queue = deque()
            queue.append(src)
            visited = set()
            while queue:
                for i in range(len(queue)):
                    course = queue.popleft()                    
                    if course == dst:
                        return True
                    if course in visited:
                        continue
                    visited.add(course)
                    for nb in adj[course]:
                        if nb not in visited:
                            queue.append(nb)
            return False
            
        adj = defaultdict(list)
        for precourse, course in prerequisites:
            adj[precourse].append(course)
        ans = []
        for src, dst in queries:
            ans.append(bfs(src, dst)) 
        return ans
