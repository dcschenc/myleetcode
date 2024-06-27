class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(idx, path):            
            if idx == n:
                res.append(path)
                return            
            backtrack(idx + 1, path + s[idx])
            if s[idx].isalpha():
                if s[idx].islower():
                    backtrack(idx + 1, path + s[idx].upper())
                else:
                    backtrack(idx + 1, path + s[idx].lower())
            # for i in range(idx+1, n+1):
            # backtrack(idx + 1, path + s[idx])                
            # if s[idx].islower():
            #     backtrack(idx + 1, path + s[idx].upper())
            # else:
            #     backtrack(idx + 1, path + s[idx].lower())             
        res = []
        n = len(s)
        backtrack(0, '')
        return res