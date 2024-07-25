class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_cnt = 0
        self.prefix_cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur.children[c].prefix_cnt += 1
            cur = cur.children[c]
        cur.word_cnt += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.word_cnt        

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.prefix_cnt

    def erase(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur.children[c].prefix_cnt -= 1
            cur = cur.children[c]
        cur.word_cnt -= 1
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)