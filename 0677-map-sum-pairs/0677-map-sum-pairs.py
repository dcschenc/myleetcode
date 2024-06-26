class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.val = 0
        self.is_end = False
        
class MapSum:
    def __init__(self):
        self.root = Trie()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = Trie()            
            cur = cur.children[idx]       
        cur.is_end = True
        cur.val = val

    def sum(self, prefix: str) -> int:
        def dfs(node):
            if node.is_end == True:
                ans[0] += node.val
            for i in range(26):
                if node.children[i]:
                    dfs(node.children[i])

        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')            
            cur = cur.children[idx]
            if cur is None:
                return 0
        ans = [0]
        dfs(cur)
        return ans[0]


# class MapSum:
#     def __init__(self):
#         self.hm = {}

#     def insert(self, key: str, val: int) -> None:
#         self.hm[key] = val

#     def sum(self, prefix: str) -> int:
#         ans = 0
#         for k in self.hm:
#             if k.startswith(prefix):
#                 ans += self.hm[k]
#         return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)