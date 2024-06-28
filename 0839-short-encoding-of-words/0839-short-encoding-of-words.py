class Trie:
    def __init__(self):
        self.children = [None] * 26

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # hm = defaultdict(list)        
        # words.sort(key=lambda x: len(x), reverse=True)
        # n = len(words)
        # exclude = set()
        # for i in range(n):
        #     if words[i] not in exclude:
        #         for j in range(1, len(words[i])):
        #             exclude.add(words[i][j:])
        # cnt = 0
        # words = set(words) - exclude
        # for w in words:
        #     cnt += len(w) + 1
        # return cnt

        
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0820.Short%20Encoding%20of%20Words

        def dfs(cur, cnt):
            is_leaf = True
            for i in range(26):
                if cur.children[i]:
                    is_leaf = False
                    dfs(cur.children[i], cnt + 1)
            if is_leaf:
                ans[0] += cnt + 1
                
        root = Trie()
        for word in words:
            cur = root
            for c in word[::-1]:
                idx = ord(c) - ord('a')
                if not cur.children[idx]:
                    cur.children[idx] = Trie()
                cur = cur.children[idx]            

        ans = [0]
        dfs(root, 0)
        return ans[0]