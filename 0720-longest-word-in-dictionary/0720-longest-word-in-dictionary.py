class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # words.sort(key=lambda x: (-len(x), x))
        # words_set = set(words)
        # for i, w in enumerate(words):
        #     found = True
        #     for i in range(1, len(w)):
        #         if w[:i] not in words_set:
        #             found = False
        #             break
        #     if found:
        #         return w
        # return ""

        def dfs(cur, path):
            if cur != trie.root and cur.is_word is False:
                return
            nonlocal mx, ans
            # if len(cur.children) == 0:
            if cur.is_word:
                if len(path) > mx:
                    mx = len(path)
                    ans = ''.join(path)
                elif len(path) == mx and ans  > ''.join(path):
                    ans = ''.join(path)
                # return
            for c, node in cur.children.items():
                dfs(node, path + [c])

        trie = Trie()
        for word in words:
            trie.insert(word)
        mx, ans = 0, ''
        dfs(trie.root, [])
        return ans


