class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []
        for val in arr:
            if val not in ['.', '..', '']:
                stack.append(val)
            else:
                if val == '..' and stack:
                    stack.pop()
                    
        return '/' + '/'.join(stack)
