class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:    
        # m = len(s)
        # dp = [False] * (m+1)
        # dp[0] = True
        # for i in range(1, m+1):
        #     for j in range(i):
        #         if s[j:i] in wordDict:
        #             dp[i] = dp[i] | dp[j]           
        # return dp[-1]

        ### method 2, improved ###
        root = TrieNode()
        for word in wordDict:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.is_word = True

        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                cur = root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in cur.children:
                        # No words exist
                        break
                    cur = cur.children[c]
                    if cur.is_word:
                        dp[j] = True
        return dp[-1]

        
        # for i in range(1,m+1):
        #     match = False
        #     for w in wordDict:
        #         l = len(w)
        #         if i-l >= 0 and s[i-l:i] == w:
        #             if dp[i-l]:
        #                 match = True
        #                 break
        #     dp[i] = match
        # return dp[-1]
