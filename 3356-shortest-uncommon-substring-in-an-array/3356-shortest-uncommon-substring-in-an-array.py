class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = set() # can replace with # of word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, num):
        lengh = len(word)
        for i in range(lengh):
            cur = self.root
            for j in word[i:]:
                if j not in cur.children:
                    cur.children[j] = TrieNode()
                cur = cur.children[j]
                cur.isWord.add(num)

    def find(self, word):
        lengh = len(word)
        ans = []
        for i in range(lengh):
            cur = self.root
            cur_str = ''
            for c in word[i:]:
                cur_str += c
                cur = cur.children[c]
                if len(cur.isWord) == 1:
                    ans.append(cur_str)
                    break
        return sorted(ans, key=lambda x:(len(x),x))[0] if ans else ''

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        t = Trie()
        for idx, word in enumerate(arr):
            t.insert(word, idx)

        ans = []
        for word in arr:
            ans.append(t.find(word))
        return ans