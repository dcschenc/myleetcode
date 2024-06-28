class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):                
            if node == len(graph)-1:                
                res.append(path[:] + [node])
                return
            path.append(node)  
            for nb in graph[node]:
                dfs(nb, path)
            path.pop()
        
        path = []
        res = []
        dfs(0, path)
        return res
