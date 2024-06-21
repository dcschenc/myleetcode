class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_seen = {}
        for i in range(len(s)):
            last_seen[s[i]] = i
        for i in range(len(s)):
            if s[i] in stack:
                continue
            while stack and s[i] < stack[-1] and last_seen[stack[-1]] > i:
                stack.pop()            
            stack.append(s[i])
        return ''.join(stack)