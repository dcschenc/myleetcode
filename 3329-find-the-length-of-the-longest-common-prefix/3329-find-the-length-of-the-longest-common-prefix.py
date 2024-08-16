class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word):
        cur = self.root
        common = 0
        for c in word:
            if c not in cur.children:
                return common
            cur = cur.children[c]
            common += 1
        return common


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        ans = 0
        for word in arr1:
            trie.add_word(str(word))
        
        for word in arr2:
            length = trie.search(str(word))
            ans = max(length, ans)
        
        return ans

        # set1, set2 = set(), set()
        # for num in arr1:
        #     num = str(num)
        #     for i in range(len(num)):
        #         set1.add(num[:i+1])
        # for num in arr2:
        #     num = str(num)
        #     for i in range(len(num)):
        #         set2.add(num[:i+1])
        # return max([len(prefix) for prefix in set1 & set2], default=0)