class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.is_end = True

class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)        

    def search(self, searchWord: str) -> bool:
        def dfs(i, diff, cur):
            if i == n:
                return diff == 1 and cur.is_end is True
          
            res = False
            for k, child in cur.children.items():
                if k == searchWord[i]:
                    if dfs(i + 1, diff, child):
                        res = True
                        break
                else:
                    if diff == 0 and dfs(i + 1, diff + 1, child):
                        res = True
                        break
            return res        
        n = len(searchWord)
        return dfs(0, 0, self.trie)
       


# class MagicDictionary:
#     def __init__(self):
#         self.s = set()       

#     def buildDict(self, dictionary: List[str]) -> None:
#         for w in dictionary:
#             self.s.add(w)

#     def search(self, searchWord: str) -> bool:
#         for i, c in enumerate(searchWord):
#             for r in string.ascii_lowercase:
#                 if c != r and searchWord[:i] + r + searchWord[i+1:] in self.s:
#                     return True
#         return False
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)