class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        i, n, m = 0, len(s), len(part)
        part = list(part)
        while i < n:
            stack.append(s[i])
            if len(stack) >= m and stack[-m:] == part:
                stack = stack[:-m]
                # for j in range(m):
                #     stack.pop()
            i += 1
        return ''.join(stack)