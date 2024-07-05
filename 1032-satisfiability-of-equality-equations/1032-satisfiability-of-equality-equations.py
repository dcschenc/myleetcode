from collections import defaultdict
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = list(range(26))
        def find_root(x):
            if x != root[x]:
                root[x] = find_root(root[x])
            return root[x]
        
        def union(x, y):
            rootX, rootY = find_root(x), find_root(y)
            if rootX != rootY:
                root[rootY] = rootX
        
        for eq in equations:
            if eq[1] == '=':
                x, y = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
                union(x, y)
                
        for eq in equations:
            if eq[1] == '!':
                x, y = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
                if find_root(x) == find_root(y):
                    return False
        return True
        