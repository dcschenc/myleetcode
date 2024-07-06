class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
        
        # res = s[0]
        # i, n = 0, len(s)
        # while i < n:
        #     j = i + 1
        #     while j < n and s[j] == res[-1]:
        #         j += 1
        #     if j < n:
        #         res += s[j]
        #     # print(i, j, res)
        #     i = j
        # return res

