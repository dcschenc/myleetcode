class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_open = []
        stack_star = []

        for i, char in enumerate(s):
            if char == '(':
                stack_open.append(i)
            elif char == '*':
                stack_star.append(i)
            else:
                if stack_open:
                    stack_open.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False

        while stack_open and stack_star:
            if stack_open[-1] > stack_star[-1]:
                return False  # '*' cannot replace '(' after this position
            stack_open.pop()
            stack_star.pop()

        return not stack_open