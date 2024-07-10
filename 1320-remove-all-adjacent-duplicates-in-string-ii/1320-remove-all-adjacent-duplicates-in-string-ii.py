class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                if stack[-1][1] == k - 1:
                    for i in range(k - 1):
                        stack.pop()
                else:
                    stack.append((c, stack[-1][1] + 1))
            else:
                stack.append((c, 1))
        return ''.join([c for c, cnt in stack])

        # stack = []
        # stack2 = [1]
        # cnt = 1
        # for i in range(len(s)):            
        #     if stack:
        #         if s[i] == stack[-1]:
        #             cnt += 1
        #         else:
        #             stack2.append(cnt)
        #             cnt = 1
        #     stack.append(s[i])
        #     if cnt == k:
        #         for _ in range(k):
        #             stack.pop()
        #         if stack2:
        #             cnt = stack2.pop()
        # return ''.join(stack)