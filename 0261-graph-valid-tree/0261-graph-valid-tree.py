class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for edge in edges:
            # Cycle detected
            if uf.find(edge[0]) == uf.find(edge[1]):
                return False  
            uf.union(edge[0], edge[1])
        # Check if there is exactly one connected component
        return len(set(uf.find(i) for i in range(n))) == 1

        graph = defaultdict(list)        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        visited = set()
        def dfs(root):
            visited.add(root)
            for node in graph[root]:
                if node in visited:
                    continue
                dfs(node)
            
        dfs(0)
        return len(visited) == n and len(edges) == n - 1