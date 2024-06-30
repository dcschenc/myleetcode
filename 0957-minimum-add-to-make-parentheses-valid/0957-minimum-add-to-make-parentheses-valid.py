class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0900-0999/0921.Minimum%20Add%20to%20Make%20Parentheses%20Valid
        stack = []        
        count = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if c == ')' and stack and stack[-1] == '(':
                    stack.pop()
                else:
                    count += 1
           
        return len(stack) + count