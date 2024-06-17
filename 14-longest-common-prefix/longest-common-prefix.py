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

    def search_prefix(self, word, n):
        cur = self.root
        ans = ''
        for c in word:
            if len(cur.children) != 1 or cur.word is True:
                return ans
            ans += c
            cur = cur.children[c]
        return ans

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ans = ""
        # i, n = 0, len(strs)
        # while True:
        #     common = None
        #     for word in strs:
        #         if i < len(word):
        #             if common is None:
        #                 common = word[i]
        #             elif common != word[i]:
        #                 return ans
        #         else:
        #             return ans
        #     ans += common
        #     i += 1
        # return ans
        
        trie = Trie()
        for s in strs:
            trie.insert(s)
        
        return trie.search_prefix(strs[0], len(strs))