class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if t == '+':
                    tmp = op1 + op2
                if t == '-':
                    tmp = op1 - op2
                if t == '*':
                    tmp = op1 * op2
                if t == '/':
                    tmp = int(op1/op2)                    
                stack.append(tmp)
            else:
                stack.append(t)
        # print(stack)
        return int(stack.pop())