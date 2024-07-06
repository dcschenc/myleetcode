class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:       
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1059.All%20Paths%20from%20Source%20Lead%20to%20Destination
        @cache
        def dfs(i):
            if i == destination:
                return not g[i]
            if i in vis or not g[i]:
                return False
            vis.add(i)
            for j in g[i]:
                if not dfs(j):
                    return False
            return True

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
        vis = set()
        return dfs(source)

        
        # def dfs(node):
        #     # Check if a cycle is detected
        #     if node in visited:
        #         return False

        #     # Check if the destination is reached
        #     if not graph[node]:
        #         return node == destination

        #     visited.add(node)

        #     # Recursively check all neighbors
        #     for neighbor in graph[node]:
        #         if not dfs(neighbor):
        #             return False

        #     visited.remove(node)
        #     return True

        # graph = defaultdict(list)
        # # Build the graph
        # for u, v in edges:
        #     graph[u].append(v)

        # visited = set()

        # return dfs(source) if dfs(source) else False 

        # graph = defaultdict(list)
        # # Build the graph
        # for u, v in edges:
        #     graph[u].append(v)
        # visited = set()
        # return dfs(source)
        
        # def dfs(node, path):
        #     if node not in graph:
        #         end.add(node)
        #         return             
        #     if node in path:
        #         return False
        #     if node in visited:
        #         return
        #     path.append(node)
        #     visited.add(node)
        #     for v in graph[node]:
        #         if dfs(v, path) is False:
        #           return False
        #     path.pop()
        
        # graph = defaultdict(list)
        # for u, v in edges:
        #     graph[u].append(v)
        # end = set()
        # visited = set()
        # res = dfs(source, [])
        # if res == False:
        #   return False        
        # if len(end) == 0 or len(end) == 1 and destination in end:
        #     return True
        # return False