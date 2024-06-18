class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []        
        left, right = n, n
        stack = [('', left, right)]
        
        while stack:
            ans, left, right = stack.pop()
            if left > 0:
                stack.append((ans + '(', left - 1, right))
            if right > 0 and left < right:
                stack.append((ans + ')', left, right - 1))
            if left == 0 and right == 0:
                res.append(ans)
                
        return res
            

        def backtrack(left, right, path):
            if left == 0 and right ==0:
                res.append(path)
            if left > 0:
                backtrack(left - 1, right, path + '(')
            if right > 0 and left < right:
                backtrack(left, right - 1, path + ')')
            
        res = []
        backtrack(n, n, '')
        return res