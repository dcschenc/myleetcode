class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(i):
            if i == len(s):
                ans.append(" ".join(path[:]))
                return
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    path.append(s[i:j])              
                    backtrack(j)
                    path.pop()
        
        ans = []
        path = []
        backtrack(0)
        return ans