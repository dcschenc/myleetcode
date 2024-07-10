class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c != ')':
                stack.append(c)
            else:
                t = []
                while stack and stack[-1] != '(':
                    t.append(stack.pop())
                if stack:
                    stack.pop()
                stack.extend(t)
        return ''.join(stack)
