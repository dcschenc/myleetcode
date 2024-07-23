class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

class Solution:
    def countDistinct(self, s: str) -> int:  
        # n = len(s)
        # ans = set()
        # for i in range(n):   # O(n ** 3)
        #     for j in range(i, n):
        #         ans.add(s[i:j+1])
        # return len(ans)

        root = TrieNode()    
        count = 0
        n = len(s)
        for i in range(n):   # O(n ** 2)
            cur = root    
            for j in range(i, n):
                # when char not present add it to the trie
                ch = ord(s[j]) - ord('a')                
                if not cur.children[ch]:
                    cur.children[ch] = TrieNode()
                    count += 1
                cur = cur.children[ch]    
        return count