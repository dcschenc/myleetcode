class Solution:
    def calculate(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0200-0299/0224.Basic%20Calculator
        stk = []
        ans, sign = 0, 1
        i, n = 0, len(s)
        while i < n:
            if s[i].isdigit():
                x = 0
                j = i
                while j < n and s[j].isdigit():
                    x = x * 10 + int(s[j])
                    j += 1
                ans += sign * x
                i = j - 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stk.append(ans)
                stk.append(sign)
                ans, sign = 0, 1
            elif s[i] == ")":
                ans = stk.pop() * ans + stk.pop()
            i += 1
        return ans
        
        stack = []
        result = 0
        sign = 1  # 1 represents positive, -1 represents negative
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
            elif char == '+':
                sign = 1
                i += 1
            elif char == '-':
                sign = -1
                i += 1
            elif char == '(':
                stack.append((result, sign))
                result = 0
                sign = 1
                i += 1
            elif char == ')':
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result
                i += 1
            elif char.isspace():
                i += 1
            else:
                # Handle other characters (invalid input)
                return 0

        return result