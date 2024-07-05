class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for c in s:            
        #     stack.append(c)
        #     # print(stack, stack[-3:])
        #     if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
        #         stack.pop()
        #         stack.pop()
        #         stack.pop()
        #         # stack = stack[:-3]
        # return len(stack) == 0

        stack = []

        for char in s:
            if char == 'c':
                if len(stack) < 2 or stack[-1] != 'b' or stack[-2] != 'a':
                    return False
                stack.pop()  # Remove 'a'
                stack.pop()  # Remove 'b'
            else:
                stack.append(char)

        return not stack  # The string is valid if the stack is empty
