class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
        
        root = [i for i in range(n)]
        rank = [1] * n
        for x, y in edges:
            union(x, y)
        groups = set()
        
        # print(root)
        for i in range(n):
            node = find(i)
            if node not in groups:
                groups.add(node)
        return len(groups)




        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for nb in graph[node]:
                dfs(nb)
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1
        return count