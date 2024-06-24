class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        i, n = 0, len(expression)
        expression = expression[::-1]
        while i < n:
            if stack and stack[-1] == '?':
                stack.pop()
                op1 = stack.pop()
                stack.pop()
                op2 = stack.pop()
                if expression[i] == 'T':
                    stack.append(op1)
                else:
                    stack.append(op2)
            else:
                stack.append(expression[i])
            i += 1

        return stack[-1]


        # stack = []
        # i, n = 0, len(expression)
        # while i < n:
        #     print(expression[i], stack)
        #     if stack and stack[-1] == ':':
        #         stack.pop()
        #         op1 = stack.pop()
        #         stack.pop()
        #         cond  = stack.pop()
        #         if cond == 'T':
        #             stack.append(op1)
        #         else:
        #             stack.append(expression[i])
        #     else:
        #         stack.append(expression[i])
        #     i += 1
        # return stack[-1]

                