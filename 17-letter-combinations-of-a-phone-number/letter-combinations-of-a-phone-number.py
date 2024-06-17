class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(idx, path):
            if idx == n:
                res.append(path)
                return
            for c in hm[digits[idx]]:
                backtrack(idx + 1, path + c)
        
        n, res = len(digits), []
        if n == 0: return res
        hm = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        backtrack(0, '')        
        return res
                

        res = ''
        digit_m = {'2': ['a', 'b', 'c'],'3':['d','e','f'],'4':['g', 'h', 'i'], 
        '5': ['j','k','l'], '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],
        '9':['w','x','y','z']}
        for d in digits:            
            chars = digit_m[d]
            if res == '':
                res = chars
            else:
                current_res = []
                for item in res:
                    for c in chars:
                        new_item = item + c
                        current_res.append(new_item)
                res = current_res
        return res
                