class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        removed = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    removed.append(i)
                    count += 1
        for c, i in stack:
            removed.append(i)
        res = ''
        for i in range(len(s)):
            if i not in removed:
                res += s[i]
        return res