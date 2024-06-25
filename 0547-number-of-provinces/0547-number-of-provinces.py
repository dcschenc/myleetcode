class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
            
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
                return 1
            return 0
            
        res = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    res -= union(i, j)
        return res
       

        def dfs(i):
            visited.add(i)
            for k in range(len(isConnected[i])):
                if i!= k and isConnected[i][k] == 1 and k not in visited:
                    dfs(k)

        m, n = len(isConnected), len(isConnected[0])
        visited = set()
        cnt = 0
        for i in range(m):
            for j in range(n):
                if i not in visited:
                    dfs(i)
                    cnt += 1
        return cnt