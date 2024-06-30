class Solution:  
    def removeStones(self, stones: List[List[int]]) -> int:
        root = {(u, v): (u, v) for u, v in stones}        
        def find_root(x):
            if root[x] == x:
                return x
            root[x] = find_root(root[x])
            return root[x]

        def union(x, y):
            root1 = find_root(x)
            root2 = find_root(y)
            if root1 != root2:
                root[root2] = root1

        for i in range(len(stones)):
            for j in range(i, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union((stones[i][0], stones[i][1]), (stones[j][0], stones[j][1]))

        # Count the number of distinct roots
        roots = set()
        for i in range(len(stones)):
            roots.add(find_root((stones[i][0], stones[i][1])))

        return len(stones) - len(roots)