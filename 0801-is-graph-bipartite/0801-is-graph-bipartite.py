class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n  # 0: uncolored, 1: color A, -1: color B

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False  # The graph is not bipartite
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            return True

        for i in range(n):
            if colors[i] == 0 and not dfs(i, 1):
                return False

        return True


        setA = set()
        setB = set()
        for i in range(len(graph)):
            if not set(graph[i]).intersection(setA):
                setA.add(i)
            elif not set(graph[i]).intersection(setB):
                setB.add(i)
            else:
                return False
        return True

