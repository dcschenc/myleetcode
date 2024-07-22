class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        i, n = 0, len(command)
        while i < n:
            if command[i] == 'G':
                ans += 'G'
                i += 1
            elif command[i:i+2] == '()':
                ans += 'o'
                i = i + 2
            else:
                ans += 'al'
                i = i + 4
        return ans