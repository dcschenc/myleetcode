class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ''
        for i, c in enumerate(s):
            if c == '[':
                stack.append(c)
            elif c in '0123456789':               
                stack.append(c)
            elif c == ']':
                substr_arr = []
                while stack and stack[-1] != '[':
                    substr_arr.append(stack.pop())
                stack.pop()
                tmp = ''
                while stack and stack[-1] in '0123456789':
                    tmp += stack.pop()                
                repeat = int(tmp[::-1])
                stack.append(''.join(substr_arr[::-1])*repeat)
            else:
                stack.append(c)
        result = ''.join(stack)
        return result
                