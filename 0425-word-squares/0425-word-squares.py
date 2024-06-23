class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.v = []

    def insert(self, w, i):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.v.append(i)

    def search(self, w):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return []
            node = node.children[idx]
        return node.v


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def dfs(t):
            if len(t) == len(words[0]):
                ans.append(t[:])
                return
            idx = len(t)
            pref = [v[idx] for v in t]
            indexes = trie.search(''.join(pref))
            for i in indexes:
                t.append(words[i])
                dfs(t)
                t.pop()

        trie = Trie()
        ans = []
        for i, w in enumerate(words):
            trie.insert(w, i)
        for w in words:
            dfs([w])
        return ans

        # def is_word_square(path):
        #     nonlocal n
        #     for i in range(n):
        #         row_w = path[i]
        #         col_w = ''
        #         for j in range(n):
        #             col_w += path[j][i]
        #         if row_w != col_w:
        #             return False
        #     return True

        def backtrack(idx, cnt, path):
            nonlocal n
            if cnt == n:
                # if is_word_square(path):
                res.append(path[:])
                return
            if cnt >= n: 
                return

            prefix = ''
            for k in range(cnt):
                prefix += path[k][cnt]

            for i in range(m):
                # if cnt > 0:
                #     stop = False
                    # print(prefix, words[i][:cnt])
                if prefix == words[i][:cnt]: 
                    backtrack(i, cnt + 1, path + [words[i]])
        
        m, n, res = len(words), len(words[0]), []
        backtrack(0, 0, [])
        return res