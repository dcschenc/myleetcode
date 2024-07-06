from collections import defaultdict
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        N = n
        # Create an adjacency list
        graph = [[] for _ in range(N + 1)]
        # Populate the adjacency list
        for path in paths:
            graph[path[0]].append(path[1])
            graph[path[1]].append(path[0])

        # Initialize the result array with zeros
        result = [0] * N
        # Iterate through each garden and assign a flower type
        for i in range(1, N + 1):
            available_colors = {1, 2, 3, 4}
            # Check the colors of adjacent gardens
            for neighbor in graph[i]:
                if result[neighbor - 1] in available_colors:
                    available_colors.remove(result[neighbor - 1])
            # Assign the first available color to the current garden
            result[i - 1] = available_colors.pop()

        return result

        # def dfs(node):
        #     nbs = adj[node]
        #     nb_colors = set(colors.get(v) for v in nbs)
        #     valid_colors = set([1,2,3,4,5]) - nb_colors
        #     colors[node] = valid_colors.pop()
        #     for v in nbs:
        #         if v not in colors:
        #             dfs(v)

        # adj = defaultdict(list)
        # for u, v in paths:
        #     adj[u].append(v)
        #     adj[v].append(u)
        # colors = {}
        # for i in range(1, n+1):
        #     if i not in colors:
        #         dfs(i)     

        # return [colors[i] for i in range(1, n + 1)]