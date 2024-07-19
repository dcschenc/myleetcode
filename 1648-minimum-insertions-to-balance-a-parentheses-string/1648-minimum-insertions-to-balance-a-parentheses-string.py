class Solution:
    def minInsertions(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1541.Minimum%20Insertions%20to%20Balance%20a%20Parentheses%20String
        ans = x = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                # 待匹配的左括号加 1
                x += 1
            else:
                if i < n - 1 and s[i + 1] == ')':
                    # 有连续两个右括号，i 往后移动
                    i += 1
                else:
                    # 只有一个右括号，插入一个
                    ans += 1
                if x == 0:
                    # 无待匹配的左括号，插入一个
                    ans += 1
                else:
                    # 待匹配的左括号减 1
                    x -= 1
            i += 1
        # 遍历结束，仍有待匹配的左括号，说明右括号不足，插入 x << 1 个
        ans += x << 1
        return ans
        
        # stack = []
        # insertions = 0
        # i = 0
        # while i < len(s):
        #     if s[i] == '(':
        #         stack.append('(')
        #         i += 1
        #     elif s[i] == ')':
        #         if i + 1 < len(s) and s[i + 1] == ')':
        #             if stack:
        #                 stack.pop()
        #             else:
        #                 insertions += 1
        #             i += 2
        #         else:
        #             if stack:
        #                 stack.pop()
        #                 insertions += 1
        #             else:
        #                 insertions += 2
        #             i += 1

        # insertions += 2 * len(stack)

        # return insertions

        stack = []
        ans = 0

        for c in s:
            if c == '(':
                stack.append('(')
            else:
                if not stack:
                    ans += 1  # Unmatched closing parenthesis, need to insert an opening parenthesis
                elif stack:
                    stack.pop()

        ans += 2 * len(stack)  # Add insertions for unmatched opening parentheses

        return ans

