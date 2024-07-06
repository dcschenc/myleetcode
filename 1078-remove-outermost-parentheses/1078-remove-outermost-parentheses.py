class Solution:
    # Remove Outermost Parentheses" is to iterate through the input string and keep track of the outermost parentheses. The idea is to append parentheses to the result string if they are not the outermost ones.
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0
        
        for char in s:
            if char == '(' and opened > 0:
                result.append(char)
            elif char == ')' and opened > 1:
                result.append(char)

            if char == '(':
                opened += 1
            else:
                opened -= 1

        return ''.join(result)