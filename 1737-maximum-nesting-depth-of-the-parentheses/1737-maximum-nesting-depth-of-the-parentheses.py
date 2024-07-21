class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        i, ans = 0, 0
        for c in s:
            if c == '(':
                stack.append(c)
                ans = max(ans, len(stack))
            elif c == ')':
                stack.pop()
        return ans
        