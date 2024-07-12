class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if len(node.words) < 3:
                node.words.append(word)

    def prefixSearch(self, pref):  ### character by character
        node = self.root
        ans = []
        for c in pref:
            if c not in node.children:
                return ans + [[] for _ in range(len(pref) - len(ans))]
            node = node.children[c]
            ans.append(node.words[:])
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in sorted(products):
            trie.insert(product)
        return trie.prefixSearch(searchWord)

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         cur = self.root
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
#             cur = cur.children[c]
#         cur.word = True

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         def dfs(cur, path):
#             if cur.word is True:
#                 words.append(path)
#             for c in cur.children.keys():
#                 # path += c
#                 dfs(cur.children[c], path + c)
#                 # path = path[:-1]

#         trie = Trie()
#         for product in products:
#             trie.insert(product)        
#         res = []
#         cur = trie.root
#         for i, c in enumerate(searchWord):
#             if c not in cur.children:
#                 for j in range(i, len(searchWord)):
#                     res.append([])
#             else:
#                 words = []
#                 dfs(cur.children[c], searchWord[:i+1])
#                 words.sort()
#                 if len(words) > 3:                
#                     words = words[:3]
#                 res.append(words)
#                 cur = cur.children[c]
#         return res


