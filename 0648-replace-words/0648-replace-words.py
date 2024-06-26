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
        replace = ''
        for c in word:            
            if c not in cur.children:
                return word
            replace += c           
            cur = cur.children[c]
            if cur.word is True:
                return replace
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = ''
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        for w in sentence.split(' '):
            ans += trie.search(w) + " "

        return ans[:-1]

        # ans = ''
        # for w in sentence.split(' '):
        #     root = w
        #     for d in dictionary:
        #         if len(d) <= len(w) and w[:len(d)] == d:
        #             if len(root) > len(d):
        #                 root = d
        #     ans += root + " "
        # return ans[:-1]
                    