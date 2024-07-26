# https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1858.Longest%20Word%20With%20All%20Prefixes
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
    
    def search(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
            if cur.word is False:
                return False
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        mx, ans = 0, ''
        for word in words:
            if (len(word) > mx or len(word) == mx and word < ans) and trie.search(word):
                ans = word
                mx = len(word)
        return ans