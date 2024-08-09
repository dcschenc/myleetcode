class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # d = set(dictionary)
        # n = len(s)
        # dp = [0] * (n + 1)
        # for i in range(n):   ### O(n**3)
        #     dp[i + 1] = dp[i] + 1
        #     j = i
        #     while j >= 0:
        #         if s[j:i+1] in d:
        #             dp[i+1] = min(dp[i+1], dp[j]) 
        #         j -= 1
        # return dp[-1]
        
        def buildTrie(dictionary):
            root = TrieNode()
            for word in dictionary:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_word = True
            return root
        
        n = len(s)
        root = buildTrie(dictionary)
        dp = [0] * (n + 1)
        
        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    dp[start] = min(dp[start], dp[end + 1])        
        return dp[0]
    
