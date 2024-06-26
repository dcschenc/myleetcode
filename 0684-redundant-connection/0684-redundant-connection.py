from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # graph = collections.defaultdict(set)
        # def dfs(source, target):
        #     if source not in seen:
        #         seen.add(source)
        #         if source == target: return True
        #         return any(dfs(nei, target) for nei in graph[source])

        # for u, v in edges:
        #     seen = set()
        #     if u in graph and v in graph and dfs(u, v):
        #         return u, v
        #     graph[u].add(v)
        #     graph[v].add(u)

        # def dfs(node, parent):
        #     if node in visited:
        #         return True     
        #     # path.append(node)
        #     visited.add(node)
        #     for nb in graph[node]:
        #         if nb != parent:
        #             res = dfs(nb, node)
        #             if res is True:
        #                 return True
        #     # path.pop()
        #     return False

        # for i in range(len(edges)-1, -1, -1):            
        #     graph = defaultdict(list)
        #     start = -1
        #     for j in range(len(edges)):
        #         if j != i:
        #             start = edges[j][0]
        #             graph[edges[j][0]].append(edges[j][1])
        #             graph[edges[j][1]].append(edges[j][0])
        #     # print(start)
        #     # print(graph)
        #     visited = set()
        #     res = dfs(start, -1)
        #     if res is False and len(visited) == len(edges):
        #         return edges[i]


        parent = [i for i in range(len(edges) + 1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
            else:
                return True  # Redundant connection found

        for edge in edges:
            if union(edge[0], edge[1]):
                return edge
            
        