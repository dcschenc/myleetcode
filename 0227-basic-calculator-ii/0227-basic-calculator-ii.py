class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)           
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/num)
                num = 0
                sign = c
        return sum(stack)

# >>> -3//2
# -2
# >>> int(-3/2)
# -1
