class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        word = word.split('/')
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # folder.sort()
        # ans = [folder[0]]
        # for f in folder[1:]:
        #     m, n = len(ans[-1]), len(f)
        #     if not (ans[-1] == f[:m] and f[m] == '/'):
        #         ans.append(f)
        # return ans

        def dfs(node, cur):
            if node.word is True:
                res.append('/'.join(cur))
                return
            for c in node.children.keys():
                cur.append(c)
                dfs(node.children[c], cur)
                cur.pop()

        trie = Trie()
        for folder in folder:
            trie.insert(folder)
                    
        cur = trie.root
        res = []
        dfs(trie.root, [])
        return res