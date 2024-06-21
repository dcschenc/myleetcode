class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        def backtrack(idx, cur):
            if idx >= n:
               res.append(cur)
               return
            backtrack(idx + 1, cur + word[idx])
            if cur and cur[-1].isdigit():
                return
            for j in range(idx, n):
                backtrack(j + 1, cur + str(j - idx + 1))

        res = []        
        n = len(word)
        backtrack(0, '')
        return res