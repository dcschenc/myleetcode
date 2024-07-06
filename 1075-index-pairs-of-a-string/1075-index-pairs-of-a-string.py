class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()        
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:  
        # words = set(words)  # O(n*s)
        # ans = []
        # n = len(text)
        # for i in range(n):   ## O(m**3)
        #     for j in range(i, n):
        #         if text[i:j + 1] in words:
        #             ans.append([i, j])
        # return ans

        trie = Trie()
        for word in words:   # O(n*s)
            trie.insert(word)
        
        ans, n = [], len(text)
        for i in range(n):  # O(m ** 2)
            cur = trie.root
            for j in range(i, n):
                if text[j] not in cur.children:
                    break
                cur = cur.children[text[j]]
                if cur.word is True:
                    ans.append([i, j])
        return ans