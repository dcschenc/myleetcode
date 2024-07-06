class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(s, t):
            m, n = len(s), len(t)
            i = j = 0
            while j < n:
                while i < m and s[i] != t[j] and s[i].islower():
                    i += 1
                if i == m or s[i] != t[j]:
                    return False
                i, j = i + 1, j + 1
            while i < m and s[i].islower():
                i += 1
            return i == m

        return [check(q, pattern) for q in queries]

        # trie = Trie()
        # trie.insertPattern(pattern)
        # return trie.check(queries)        

# class TrieNode:    
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)    

# class Trie:    
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insertPattern(self, pattern: str):        
#         node = self.root        
#         for char in pattern:
#             node = node.children[char]    
    
#     def check(self, queries: list[str]):        
#         res = []        
#         for query in queries:            
#             node = self.root
#             isInserted = True            
#             for char in query:                
#                 if char.isupper() and char not in node.children:
#                     isInserted = False
#                     break                    
#                 if char.islower() and char not in node.children:
#                     continue                
#                 node = node.children[char] 
            
#             while len(node.children.keys()) > 0:                
#                 char = list(node.children.keys())[0]                
#                 if char.isupper():
#                     isInserted = False
#                     break                    
#                 node = node.children[char]
                                
#             res.append(isInserted)
            
#         return res
        