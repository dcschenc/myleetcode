class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # https://leetcode.com/problems/score-of-parentheses/editorial/
        ans = bal = 0
        for i, x in enumerate(s):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if s[i-1] == '(':
                    ans += 1 << bal
        return ans

        stack1, stack2 = [], []
        for i in range(len(s)):
            if s[i] == '(':
                stack1.append(('(', i))
            else:
                if stack1[-1][1] == i-1:
                    stack1.pop()
                    stack2.append((1, i-1))
                else:
                    num = 0
                    while stack2 and stack2[-1][1] > stack1[-1][1]:
                        num += stack2.pop()[0]
                    stack2.append((num*2, stack1[-1][1]))
                    stack1.pop()
        result = 0
        while stack2:
            result += stack2.pop()[0]
        return result