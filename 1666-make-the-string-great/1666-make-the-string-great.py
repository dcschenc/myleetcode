class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        diff = abs(ord('a') - ord('A'))
        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == diff:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)